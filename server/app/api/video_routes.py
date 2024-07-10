import jwt
import os
import shutil
import subprocess

from typing import Annotated
from fastapi import APIRouter, HTTPException, UploadFile, Response, Header, Body, File, Path
from fastapi.responses import FileResponse
from typing import List
from app.core.config import Config
from app.domain.services.video_service import VideoService
from app.domain.services.auth_service import AuthService
from app.domain.models.video import Video, UpdateVideoRequest
from app.domain.models.user import User

router = APIRouter()
video_service = VideoService()
auth_service = AuthService()

def get_and_verify_user(Authorization: str) -> User:
    if Authorization is None:
        print("User id not found")
        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    try:
        
        print(f"Authorization: {Authorization}")
        token = Authorization
        
        print("Decoding token...")
        payload = jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        print("Getting user id...")
        user_id = payload.get("sub")
        if user_id is None:
            print("User id not found")
            raise HTTPException(status_code=401, detail="Invalid JWT token")
        user = auth_service.get_user_by_id(user_id)
        print("User founded")
        return user
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Invalid JWT token")


@router.get("/", response_model=List[Video])
def get_videos(auth: Annotated[str, Header(...)]):
    try:
        print("Getting user...")
        current_user = get_and_verify_user(auth)
        print(f"user result: {current_user.id}")
        videoResponse = video_service.get_videos(user_id=current_user.id)
        print(f"Video list: {len(videoResponse)}")
        return videoResponse
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail=err.__dict__)

@router.get("/{video_id}", response_model=Video)
def get_video_by_id(auth: Annotated[str, Header(...)], video_id: Annotated[int, Path(...)]):
    current_user = get_and_verify_user(auth)
    video = video_service.get_video_by_id(video_id, current_user.id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@router.post("/", response_model=Video)
def create_video(auth: Annotated[str, Header(...)], video: Annotated[Video, Body(...)]):
    current_user = get_and_verify_user(auth)
    video.user_id = current_user.id
    created_video = video_service.create_video(video)
    return created_video

@router.put("/{video_id}", response_model=Video)
def update_video(
    auth: Annotated[str, Header(...)],
    video_id: Annotated[int, Path(...)],
    video: Annotated[UpdateVideoRequest, Body(...)],
):
    current_user = get_and_verify_user(auth)
    updated_video = video_service.update_video(video, current_user.id, video_id)
    if not updated_video:
        raise HTTPException(status_code=404, detail="Video not found")
    return updated_video


@router.delete("/{video_id}", response_model=Video)
def delete_video(auth: Annotated[str, Header(...)], video_id: Annotated[int, Path(...)]):
    current_user = get_and_verify_user(auth)
    deleted_video = video_service.delete_video(video_id, current_user.id)
    if not deleted_video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Eliminar el archivo de video
    if os.path.exists(deleted_video.url):
        os.remove(deleted_video.url)

    return deleted_video

@router.post("/upload/{video_id}", response_model=Video)
async def upload_video_file(
    auth: Annotated[str, Header(...)],
    video_id: Annotated[int, Path(...)],
    file: Annotated[UploadFile, File(...)],
):
    try:
        user = get_and_verify_user(auth)
        # Guardar el archivo de video en el servidor
        file_name = f'video_{video_id}.mp4'
        file_location = os.path.join(f"{os.getcwd()}{Config.VIDEO_DIRECTORY}", file_name)
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)

        video = video_service.get_video_by_id(video_id, user.id)
        
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        
        # Actualizar la información del video en la base de datos
        video.url = file_name
        updated_video = video_service.update_video(UpdateVideoRequest(**video.model_dump()), user.id, video.id)

        return updated_video
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stream/{video_id}")
def stream_video(
    auth: Annotated[str, Header(...)],
    video_id: Annotated[int, Path(...)],
    range: Annotated[str | None, Header(...)]= None,
):
    current_user = get_and_verify_user(auth)
    video = video_service.get_video_by_id(video_id, current_user.id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    file_name=video.url
    video_path = f"{os.getcwd()}{Config.VIDEO_DIRECTORY}"
    print(f"PATH: {video_path}")
    file_size = os.path.getsize(f'{video_path}{file_name}')
    range_header = range
    if range_header:
        start, end = range_header.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else file_size - 1
        length = end - start + 1
        with open(f'{video_path}{file_name}', "rb") as video_file:
            video_file.seek(start)
            data = video_file.read(length)
        content_range = f"bytes {start}-{end}/{file_size}"
        headers = {
            'Content-Range': content_range,
            'Accept-Ranges': 'bytes',
            'Content-Length': str(length),
            'Content-Type': 'video/mp4',
        }
        return Response(data, status_code=206, headers=headers)
    return FileResponse(path=video_path, filename=file_name, media_type="video/mp4")

@router.get("/snapshot/{video_id}")
def get_video_snapshot(auth: Annotated[str, Header(...)], video_id: Annotated[int, Path(...)]):
    current_user = get_and_verify_user(auth)
    video = video_service.get_video_by_id(video_id, current_user.id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    file_name = f"{video.url}.png"
    snapshot_path = f"{os.getcwd()}{Config.VIDEO_DIRECTORY}"
    print(f"snapshot_path: {snapshot_path}")
    if os.path.exists(snapshot_path):
        print("Si existe la ruta")
        # Crear snapshot usando ffmpeg
        subprocess.call([
            'ffmpeg', '-i',
            f'{snapshot_path}{video.url}',
            '-ss',
            '00:00:01.000',
            '-vframes',
            '1',
            f'{file_name}',
        ])
    else:
        raise HTTPException(status_code=404, detail="Not found.")

    return FileResponse(path=f'{snapshot_path}{file_name}', filename=file_name, media_type="image/png")



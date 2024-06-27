import jwt
import os
import shutil
import subprocess

from typing import Annotated
from fastapi import APIRouter, HTTPException, Header, UploadFile, Response, Request, File
from fastapi.responses import FileResponse
from typing import List
from app.core.config import Config
from app.domain.services.video_service import VideoService
from app.domain.services.auth_service import AuthService
from app.domain.models.video import Video
from app.domain.models.user import User

router = APIRouter()
video_service = VideoService()
auth_service = AuthService()

def get_current_user(Authorization: str) -> User:
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
        current_user = get_current_user(auth)
        print(f"user result: {current_user.id}")
        videoResponse = video_service.get_videos(user_id=current_user.id)
        print(f"Video list: {len(videoResponse)}")
        return videoResponse
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail=err.__dict__)

@router.get("/{video_id}", response_model=Video)
def get_video_by_id(auth: Annotated[str, Header(...)], video_id: int):
    current_user = get_current_user(auth)
    video = video_service.get_video_by_id(video_id, current_user.id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@router.post("/", response_model=Video)
def update_video(auth: Annotated[str, Header(...)], video: Video):
    current_user = get_current_user(auth)
    video.user_id = current_user.id
    return video_service.update_video(video)

@router.delete("/{video_id}", response_model=Video)
def delete_video(auth: Annotated[str, Header(...)], video_id: int):
    current_user = get_current_user(auth)
    deleted_video = video_service.delete_video(video_id, current_user.id)
    if not deleted_video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Eliminar el archivo de video
    if os.path.exists(deleted_video.url):
        os.remove(deleted_video.url)

    return deleted_video

@router.post("/upload/{video_id}", response_model=Video)
async def upload_video_file(auth: Annotated[str, Header(...)], video_id: int, file: UploadFile = File(...)):
    try:
        user_id = get_current_user(auth)
        # Guardar el archivo de video en el servidor
        file_location = os.path.join(Config.VIDEO_DIRECTORY, f'video_{video_id}.mp4')
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
        
        
        video = video_service.get_video_by_id(video_id, user_id)
        
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        
        # Actualizar la información del video en la base de datos
        video.url = file_location
        updated_video = video_service.update_video(video)

        return updated_video
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stream/{video_id}")
def stream_video(request: Request, auth: Annotated[str, Header(...)], video_id: int):
    current_user = get_current_user(auth)
    video = video_service.get_video_by_id(video_id, current_user.id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    video_path = video.url
    file_size = os.path.getsize(video_path)
    range_header = request.headers.get('Range', None)
    if range_header:
        start, end = range_header.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else file_size - 1
        length = end - start + 1
        with open(video_path, "rb") as video_file:
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
    return FileResponse(video_path, media_type="video/mp4")

@router.get("/snapshot/{video_id}")
def get_video_snapshot(auth: Annotated[str, Header(...)], video_id: int):
    current_user = get_current_user(auth)
    video = video_service.get_video_by_id(video_id, current_user.id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    snapshot_path = f"{video.url}.png"
    if not os.path.exists(snapshot_path):
        # Crear snapshot usando ffmpeg
        subprocess.call(['ffmpeg', '-i', video.url, '-ss', '00:00:01.000', '-vframes', '1', snapshot_path])

    return FileResponse(snapshot_path, media_type="image/png")



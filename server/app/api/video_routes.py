import jwt

from fastapi import APIRouter, Depends, HTTPException, Header
from typing import List
from app.core.config import init_supabase, Config
from app.domain.services.video_service import VideoService
from app.domain.models.video import Video
from gotrue import User as BaseUser

router = APIRouter()
video_service = VideoService()
supabase = init_supabase()

def get_current_user(Authorization: str = Header(...)) -> BaseUser:
    try:
        token = Authorization.split(" ")[1]
        
        payload = jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid JWT token")
        userResponse = supabase.auth.admin.get_user_by_id(user_id)
        return userResponse.user
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Invalid JWT token")

@router.get("/", response_model=List[Video])
def get_videos(Authorization: str = Header(...)):
    try:
        current_user = get_current_user(Authorization)
        videoResponse = video_service.get_videos(user_id=current_user.id)
        return videoResponse
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail=err.__dict__)

@router.post("/", response_model=Video)
def upload_video(video: Video, Authorization: str = Header(...)):
    current_user = get_current_user(Authorization)
    video.user_id = current_user.id
    return video_service.upload_video(video)

@router.delete("/{video_id}", response_model=Video)
def delete_video(video_id: int, Authorization: str = Header(...)):
    current_user = get_current_user(Authorization)
    deleted_video = video_service.delete_video(video_id, current_user.id)
    if not deleted_video:
        raise HTTPException(status_code=404, detail="Video not found")
    return deleted_video

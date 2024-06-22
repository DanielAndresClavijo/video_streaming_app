from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from typing import List
from app.domain.services.video_service import VideoService
from app.domain.models.video import Video

router = APIRouter()
video_service = VideoService()

@router.get("/", response_model=List[Video])
def get_videos(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    return video_service.get_videos(user_id=user_id)

@router.post("/", response_model=Video)
def upload_video(video: Video, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    video.user_id = Authorize.get_jwt_subject()
    return video_service.upload_video(video)

@router.delete("/{video_id}", response_model=Video)
def delete_video(video_id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    video = video_service.delete_video(video_id, user_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

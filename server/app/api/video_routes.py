from fastapi import APIRouter, HTTPException
from typing import List
from app.domain.services.video_service import VideoService
from app.domain.models.video import Video

router = APIRouter()
video_service = VideoService()

@router.get("/", response_model=List[Video])
def get_videos():
    return video_service.get_videos()

@router.post("/", response_model=Video)
def upload_video(video: Video):
    return video_service.upload_video(video)

@router.delete("/{video_id}", response_model=Video)
def delete_video(video_id: int):
    video = video_service.delete_video(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

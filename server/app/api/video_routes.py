from fastapi import APIRouter, UploadFile, File
from app.domain.services.video_service import VideoService

router = APIRouter()
video_service = VideoService()

@router.get("/")
def get_videos():
    return video_service.get_videos()

@router.post("/")
def upload_video(file: UploadFile = File(...)):
    return video_service.upload_video(file)

@router.delete("/{video_id}")
def delete_video(video_id: int):
    return video_service.delete_video(video_id)

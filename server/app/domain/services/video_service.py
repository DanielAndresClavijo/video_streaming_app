from typing import List
from app.domain.models.video import Video, UpdateVideoRequest
from app.infrastructure.video_storage import VideoStorage

class VideoService:
    def __init__(self):
        self.video_storage = VideoStorage()

    def get_videos(self, user_id: int) -> List[Video]:
        return self.video_storage.get_videos(user_id=user_id)

    def get_video_by_id(self, video_id: int, user_id: int) -> Video:
        return self.video_storage.get_video_by_id(video_id, user_id)
    
    def create_video(self, video: Video) -> Video:
        return self.video_storage.create_video(video)
    
    def update_video(self, video: UpdateVideoRequest, user_id: int, video_id: int) -> Video:
        return self.video_storage.update_video(video=video, user_id=user_id, video_id=video_id)

    def delete_video(self, video_id: int, user_id: int) -> Video:
        return self.video_storage.delete_video(video_id, user_id)

from typing import List
from app.domain.models.video import Video
from app.infrastructure.video_storage import VideoStorage

class VideoService:
    def __init__(self):
        self.video_storage = VideoStorage()

    def get_videos(self, user_id: int) -> List[Video]:
        return self.video_storage.get_videos(user_id=user_id)

    def get_video_by_id(self, video_id: int, user_id: int) -> Video:
        return self.video_storage.get_video_by_id(video_id, user_id)
    
    def upload_video(self, video: Video) -> Video:
        return self.video_storage.upload_video(video)
    
    def upload_video(self, video: Video) -> Video:
        return self.video_storage.upload_video(video)

    def delete_video(self, video_id: int, user_id: int) -> Video:
        return self.video_storage.delete_video(video_id, user_id)

from typing import List
from app.domain.models.video import Video
from app.infrastructure.video_storage_supabase import SupabaseVideoStorage

class VideoService:
    def __init__(self):
        self.video_storage = SupabaseVideoStorage()

    def get_videos(self) -> List[Video]:
        return self.video_storage.get_videos()

    def upload_video(self, video: Video) -> Video:
        return self.video_storage.upload_video(video)

    def delete_video(self, video_id: int) -> Video:
        return self.video_storage.delete_video(video_id)

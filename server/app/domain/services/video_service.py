from app.infrastructure.video_storage_supabase import SupabaseVideoStorage
from fastapi import UploadFile

class VideoService:
    def __init__(self):
        self.video_storage = SupabaseVideoStorage()

    def upload_video(self, file: UploadFile):
        return self.video_storage.upload_video(file)

    def get_videos(self):
        return self.video_storage.get_videos()

    def delete_video(self, video_id: int):
        return self.video_storage.delete_video(video_id)

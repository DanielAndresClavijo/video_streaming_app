from app.core.config import init_supabase
from app.core.interfaces.video_storage_interface import VideoStorageInterface
from fastapi import UploadFile

supabase = init_supabase()

class SupabaseVideoStorage(VideoStorageInterface):
    def upload_video(self, file: UploadFile):
        bucket = 'your-bucket-name'
        response = supabase.storage().from_(bucket).upload(file.filename, file.file)
        if response.error:
            raise Exception(response.error['message'])
        return supabase.storage().from_(bucket).get_public_url(file.filename)

    def get_videos(self):
        # Implement logic to retrieve video list from Supabase
        pass

    def delete_video(self, video_id: int):
        # Implement logic to delete a video from Supabase
        pass

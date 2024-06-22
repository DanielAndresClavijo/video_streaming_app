from app.core.config import init_supabase
from app.core.interfaces.video_storage_interface import VideoStorageInterface
from app.domain.models.video import Video
from supabase import create_client, Client

supabase: Client = init_supabase()

class SupabaseVideoStorage(VideoStorageInterface):
    def upload_video(self, video: Video) -> Video:
        # Asumiendo que tienes una tabla llamada 'videos' en tu base de datos Supabase
        response = supabase.table('videos').insert(video.dict()).execute()
        if response.error:
            raise Exception(response.error.message)
        return Video(**response.data[0])

    def get_videos(self) -> list[Video]:
        response = supabase.table('videos').select('*').execute()
        if response.error:
            raise Exception(response.error.message)
        return [Video(**video) for video in response.data]

    def delete_video(self, video_id: int) -> Video:
        response = supabase.table('videos').delete().eq('id', video_id).execute()
        if response.error:
            raise Exception(response.error.message)
        if not response.data:
            return None
        return Video(**response.data[0])

from app.core.config import init_supabase
from app.core.interfaces.video_storage_interface import VideoStorageInterface
from app.domain.models.video import Video

supabase = init_supabase()

class SupabaseVideoStorage(VideoStorageInterface):
    def upload_video(self, video: Video) -> Video:
        response = supabase.table('videos').insert(video.model_dump()).execute()
        return Video(**response.data[0])

    def get_videos(self, user_id: int) -> list[Video]:
        response = supabase.table('videos').select('*').eq('user_id', user_id).execute()
        return [Video(**video) for video in response.data]

    def delete_video(self, video_id: int, user_id: int) -> Video:
        response = supabase.table('videos').delete().eq('id', video_id).eq('user_id', user_id).execute()
        if not response.data:
            return None
        return Video(**response.data[0])

from app.core.config import init_supabase
from app.core.interfaces.video_storage_interface import VideoStorageInterface
from app.domain.models.video import Video

supabase = init_supabase()

class VideoStorage(VideoStorageInterface):
    def upload_video(self, video: Video, user_id: int) -> Video:
        response = supabase.table('videos').update(video.model_dump()).eq('id', video.id).eq('user_id', user_id).execute()
        return Video(**response.data[0])

    def get_video_by_id(self, video_id: int, user_id: int) -> Video | None:
        response = supabase.table('videos').select('*').eq('id', video_id).eq('user_id', user_id).execute()
        if not response.data:
            return None
        return Video(**response.data[0])

    def get_videos(self, user_id: int) -> list[Video]:
        response = supabase.table('videos').select('*').eq('user_id', user_id).execute()
        return [Video(**video) for video in response.data]

    def delete_video(self, video_id: int, user_id: int) -> Video | None:
        response = supabase.table('videos').delete().eq('id', video_id).eq('user_id', user_id).execute()
        if not response.data:
            return None
        return Video(**response.data[0])

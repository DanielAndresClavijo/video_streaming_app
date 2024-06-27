from app.core.config import init_supabase
from app.core.interfaces.video_storage_interface import VideoStorageInterface
from app.domain.models.video import Video, UpdateVideoRequest

supabase = init_supabase()

class VideoStorage(VideoStorageInterface):

    def get_videos(self, user_id: int) -> list[Video]:
        response = supabase.table('videos').select('*').eq('user_id', user_id).execute()
        return [Video(**video) for video in response.data]

    def get_video_by_id(self, video_id: int, user_id: int) -> Video | None:
        response = supabase.table('videos').select('*').eq('id', video_id).eq('user_id', user_id).execute()
        if not response.data:
            return None
        return Video(**response.data[0])

    def create_video(self, video: Video) -> Video:
        response = supabase.table('videos').insert(video.dict()).execute()
        if not response.data:
            return None
        return Video(**response.data[0])

    def update_video(self, video: UpdateVideoRequest, user_id: int, video_id: int) -> Video:
        update_data = {}
        if video.title:
            update_data["title"] = video.title
        if video.description:
            update_data["description"] = video.description
        if video.url:
            update_data["url"] = video.url
        if video.updated_at:
            update_data["updated_at"] = video.updated_at
            
        response = supabase.table('videos').update(update_data).eq('id', video_id).eq('user_id', user_id).execute()
        return Video(**response.data[0])

    def delete_video(self, video_id: int, user_id: int) -> Video | None:
        response = supabase.table('videos').delete().eq('id', video_id).eq('user_id', user_id).execute()
        if not response.data:
            return None
        return Video(**response.data[0])

from abc import ABC, abstractmethod
from typing import List
from app.domain.models.video import Video

class VideoStorageInterface(ABC):

    @abstractmethod
    def upload_video(self, video: Video) -> Video:
        """
        Sube un video a la plataforma de almacenamiento.
        :param video: Objeto de vídeo que contiene detalles del vídeo..
        :return: Objeto de vídeo con detalles de vídeo almacenados.
        """
        pass

    @abstractmethod
    def get_videos(self, user_id: int) -> List[Video]:
        """
        Obtiene una lista de videos para un usuario específico.
        :param user_id: ID del usuario.
        :return: Lista de objetos Video.
        """
        pass

    @abstractmethod
    def delete_video(self, video_id: int, user_id: int) -> Video:
        """
        Elimina un video específico.
        :param video_id: ID del video a eliminar.
        :param user_id: ID del usuario propietario del video.
        :return: Objeto de video con detalles del video eliminado.
        """
        pass

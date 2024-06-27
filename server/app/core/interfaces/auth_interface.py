from abc import ABC, abstractmethod
from app.domain.models.video import Video
from app.domain.models.user import User 

class AuthInterface(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User:
        """
        Obtiene un usuario por medio del id
        """
        pass


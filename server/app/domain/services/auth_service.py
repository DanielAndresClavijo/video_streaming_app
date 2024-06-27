from app.infrastructure.auth_storage import AuthStorage
from app.domain.models.user import User


class AuthService:
    def __init__(self):
        self.auth = AuthStorage()

    def get_user_by_id(self, user_id: int) -> User:
        return self.auth.get_user_by_id(user_id=user_id)

from app.core.config import init_supabase
from app.core.interfaces.auth_interface import AuthInterface
from app.domain.models.user import User 

supabase = init_supabase()

class AuthStorage(AuthInterface):
    def get_user_by_id(self, user_id: str) -> User:
        userResponse = supabase.auth.admin.get_user_by_id(user_id)
        result = User.from_base_user(baseUser=userResponse.user)
        return result

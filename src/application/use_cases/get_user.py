from src.domain.exceptions.exceptions import UserNotFoundError
from src.domain.i_repos.i_user_repo import IUserRepository
from src.domain.models.user import User


class GetUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    async def get_user_by_email(self, email: str) -> User:
        user = await self._user_repository.get_user_by_email(email)
        if not user:
            raise UserNotFoundError(f"User with email {email} not found")
        return user

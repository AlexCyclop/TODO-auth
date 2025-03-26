from datetime import datetime
from uuid import uuid4

from src.domain.exceptions.exceptions import UserAlreadyExistsError
from src.domain.i_repos.i_user_repo import IUserRepository
from src.domain.models.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    @staticmethod
    def _hash_password(password: str) -> str:
        return "hashed" + password

    async def create_user(
        self,
        email: str,
        password: str,
        username: str,
        first_name: str,
        last_name: str,
    ) -> User:
        existing_user = await self._user_repository.get_user_by_email(email)
        if existing_user:
            raise UserAlreadyExistsError(f"User with email {email} already exists")

        new_user = User(
            id=uuid4(),
            email=email,
            username=username,
            hashed_password=CreateUserUseCase._hash_password(password),
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            registered_at=datetime.now(),
        )

        return await self._user_repository.create_user(new_user)

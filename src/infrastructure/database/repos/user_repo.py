from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.i_repos.i_user_repo import IUserRepository
from src.domain.models.user import User
from src.infrastructure.database.models.user import User as UserModel


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_user(self, user: User) -> User:
        user_model = UserModel(
            email=user.email,
            username=user.username,
            hashed_password=user.hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        self._session.add(user_model)
        await self._session.commit()
        await self._session.refresh(user_model)

        return User(
            id=user_model.id,
            email=user_model.email,
            username=user_model.username,
            hashed_password=user_model.hashed_password,
            first_name=user_model.first_name,
            last_name=user_model.last_name,
            is_active=user_model.is_active,
            registered_at=user_model.registered_at,
        )

    async def get_user_by_email(self, email: str) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        user_model = result.scalars().first()
        if user_model:
            return User(
                id=user_model.id,
                email=user_model.email,
                username=user_model.username,
                hashed_password=user_model.hashed_password,
                first_name=user_model.first_name,
                last_name=user_model.last_name,
                is_active=user_model.is_active,
                registered_at=user_model.registered_at,
            )
        return None

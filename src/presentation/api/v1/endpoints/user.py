from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.application.use_cases.create_user import CreateUserUseCase
from src.application.use_cases.get_user import GetUserUseCase
from src.domain.exceptions import exceptions
from src.infrastructure.database.db import get_db_session
from src.infrastructure.database.repos.user_repo import UserRepository
from src.presentation.api.v1.schemas import user as user_schemas

router = APIRouter(tags=["user"])


@router.post(
    "/create",
    response_model=user_schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_data: user_schemas.UserRegisterRequest,
    db: AsyncSession = Depends(get_db_session),
):
    user_repository = UserRepository(db)
    create_user_use_case = CreateUserUseCase(user_repository)

    try:
        user = await create_user_use_case.create_user(
            email=user_data.email,
            password=user_data.password,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )
    except exceptions.UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    return user_schemas.UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        is_active=user.is_active,
        registered_at=user.registered_at.isoformat(),
    )


@router.get("/users/{email}", response_model=user_schemas.UserResponse)
async def get_user(
    email: str,
    db: AsyncSession = Depends(get_db_session),
):
    user_repository = UserRepository(db)
    get_user_use_case = GetUserUseCase(user_repository)

    try:
        user = await get_user_use_case.get_user_by_email(email)
    except exceptions.UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

    return user_schemas.UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        is_active=user.is_active,
        registered_at=user.registered_at.isoformat(),
    )

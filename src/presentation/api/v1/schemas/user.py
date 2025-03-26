from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class BaseUserSchema(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str


class UserRegisterRequest(BaseUserSchema):
    password: str


class UserResponse(BaseUserSchema):
    id: UUID
    is_active: bool
    registered_at: datetime


class UserInDB(UserResponse):
    hashed_password: str

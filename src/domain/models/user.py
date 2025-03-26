from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class User:
    id: UUID
    email: str
    username: str
    hashed_password: str
    first_name: str
    last_name: str
    is_active: bool
    registered_at: datetime

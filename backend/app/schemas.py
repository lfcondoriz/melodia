from pydantic import BaseModel, EmailStr
from enum import Enum

class AccountType(str, Enum):
    listener = "listener"
    artist = "artist"

class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str
    account_type: AccountType = AccountType.listener

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_artist: bool
    is_active: bool

    model_config = {"from_attributes": True}

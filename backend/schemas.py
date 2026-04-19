from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: str = "listener"


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str
    is_active: bool

    model_config = {"from_attributes": True}

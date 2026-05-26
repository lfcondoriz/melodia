from fastapi import APIRouter, status
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(payload: RegisterRequest):
    return {
        "message": "registration endpoint created",
        "user": {
            "username": payload.username,
            "email": payload.email,
        },
    }

from app.models.models import User
from app.repositories import user_repository
from app.repositories.user_repository import find_by_username
from typing import Optional


def authenticate(username: str, password: str) -> Optional[User]:
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        return user
    return None
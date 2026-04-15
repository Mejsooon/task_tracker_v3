from app.models.models import User
from app.repositories import user_repository
from app.utils.helpers import get_next_id
from typing import Optional


def authenticate(username: str, password: str) -> Optional[User]:
    user = user_repository.find_by_username(username)
    if user and user.password == password:
        return user
    return None


def register(name: str, username: str, password: str) -> tuple[bool, str]:
    if not name or not username or not password:
        return False, "Wszystkie pola są wymagane."
    if user_repository.find_by_username(username):
        return False, "Użytkownik o tej nazwie już istnieje."

    user = User(
        id = get_next_id("U", "users"),
        name = name,
        username = username,
        password = password,
    )
    user_repository.save(user)
    return True, f"Konto '{name}' zostało utworzone. Możesz się zalogować."
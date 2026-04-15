from app.models.models import User
from typing import Optional
from app.core.database import execute


def _row_to_user(row: dict) -> User:
    return User(
        id=row['id'],
        name=row['name'],
        username=row['username'],
        password=row['password']
    )


def find_by_username(username: str) -> Optional[User]:
    row = execute("SELECT * FROM users WHERE username = %s", (username,), fetch="one")
    return _row_to_user(row) if row else None


def find_by_user_id(user_id: str) -> Optional[User]:
    row = execute("SELECT * FROM users WHERE id = %s", (user_id,), fetch="one")
    return _row_to_user(row) if row else None


def save(user: User) -> None:
    execute("INSERT INTO users (id, name, username, password) VALUES (%s, %s, %s, %s)",
            (user.id, user.name, user.username, user.password))
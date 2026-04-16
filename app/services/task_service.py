from app.repositories import task_repository
from app.models.models import User, Task
from typing import List


def get_active_tasks(user: User) -> List[Task]:
    return task_repository.get_by_user_and_status(user.id, "active")


def get_completed_tasks(user: User) -> List[Task]:
    return task_repository.get_by_user_and_status(user.id, "completed")
from app.models.models import User
from app.utils.helpers import clear_screen
from app.services import task_service

def user_panel(user: User):
    while True:
        clear_screen()
        active = len(task_service.get_active_tasks(user.id))
        done = len(task_service.get_completed_tasks(user.id))
        print(f"EXPOSITION TRACKER – {user.name}")
        print(f"Aktywne zadania: {active}  |  Ukończone: {done}")
        print("-" * 70)
        print("1. Utwórz nowe zadanie")
        print("2. Aktywne zadania")
        print("3. Historia zadań")
        print("4. Wyloguj się")
        print("-" * 70)

        choice = input("\nWybierz opcję: ").strip()
        if choice == "1":
            _create_task(user)
        elif choice == "2":
            _view_active(user)
        elif choice == "3":
            _view_history(user)
        elif choice == "4":
            break
        else:
            print("\n❌ Nieprawidłowa opcja.")
            input("\nNaciśnij Enter...")
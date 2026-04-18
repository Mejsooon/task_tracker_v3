from app.models.models import User
from app.utils.helpers import clear_screen, read_multiline
from app.services import task_service

def user_panel(user: User):
    while True:
        clear_screen()
        print(f"PROFIL UŻYTKOWNIKA: {user.name}")
        print("(1) Utwórz nowe zadanie")
        print("(2) Aktywne zadania")
        print("(3) Historia zadań")
        print("(4) Wyloguj się")

        user_choice = input("\nWybierz opcję: ")

        if user_choice == "1":
            _create_task(user)
        elif user_choice == "2":
            _view_active_task(user)
        elif user_choice == "3":
            _view_history(user)
        elif user_choice == "4":
            break
        else:
            print("\n❌ Nieprawidłowa opcja.")
            input("\nNaciśnij Enter...")


def _create_task(user: User):
    clear_screen()
    print("NOWE ZADANIE EKSPOZYCYJNE")
    print("=" * 60)

    try:
        difficulty = int(input("Trudność zadania (1-10): ").strip())
    except ValueError:
        difficulty = 0

    description = read_multiline("Opis zadania (zakończ pustą linią): ")
    notes = read_multiline("Dodatkowe notatki (zakończ pustą linią): ")

    ok, msg = task_service.create_task(user, difficulty, description, notes)
    print(f"\n{'✅' if ok else '❌'} {msg}")
    input("\nNaciśnij Enter...")


def _view_active_task(user: User):
    clear_screen()
    print("AKTYWNE ZADANIA")
    print("=" * 60)

    tasks = task_service.find_active_tasks(user.id)
    if not tasks:
        print("\n❌ Nie masz żadnych zadań")
        input("Naciśnij Enter...")
        return

    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task.description}")

    try:
        choice = int(input("\nWybierz zadanie (0 - powrót): ").strip())
        if choice == 0:
            return
        if not (1 <= choice <= len(tasks)):
            raise ValueError
        task = tasks[choice - 1] # Wybór zadania zgodny z indeksami, czyli od zera (0)
    except ValueError:
        print("\n❌ Nieprawidłowy wybór.")
        input("\nNaciśnij Enter...")
        return

    _read_task(user, task)


def _read_task(user: User, task):
    clear_screen()
    print(f"ZADANIE {task.id}  |  {task.description}")
    print("=" * 60)
    print(f"Poziom trudności: {task.difficulty}/10")
    print(f"Notatki: {task.additional_notes}")
    print("\n1. Oznacz jako wykonane")
    print("2. Powrót")

    if input("\nWybierz opcję: ").strip() == "1":
        _complete_task(user, task)


def _complete_task(user: User, task):
    clear_screen()
    task_service.complete_task(task)
    print("\n✅ Zadanie zostało oznaczone jako wykonane.")
    input("\nNaciśnij Enter...")


def _view_history(user: User):
    clear_screen()
    print("HISTORIA ZADAŃ")
    print("=" * 60)

    tasks = task_service.find_completed_tasks(user.id)
    if not tasks:
        print("\n❌ Nie masz żadnych zadań")
        input("\nNaciśnij Enter...")
        return

    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task.description} -> {task.difficulty}/10")
        print(f"{task.additional_notes}")

    input("\n\nNaciśnij Enter, aby wrócić...")

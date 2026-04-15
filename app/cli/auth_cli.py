from app.services import auth_service
from app.utils.helpers import clear_screen


def login_screen():
    clear_screen()
    print("BRIGHTLYNC™ – ZADANIA EKSPOZYCYJNE")
    print("=" * 70)
    print("LOGOWANIE\n" + "-" * 70)
    username = input("Nazwa użytkownika: ").strip()
    password = input("Hasło: ").strip()
    user = auth_service.authenticate(username, password)

    if user:
        print(f"\n✅ Witaj, {user.name}!")
        input("\nNaciśnij Enter, aby kontynuować...")
        return user

    print("\n❌ Nieprawidłowa nazwa użytkownika lub hasło.")
    input("\nNaciśnij Enter...")
    return None

def register_screen():
    pass
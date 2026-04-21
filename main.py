from app.utils.helpers import clear_screen
from app.cli.auth_cli import login_screen, register_screen
from app.cli.main_cli import user_panel
import logging


logging.basicConfig(
    level=logging.WARNING,       # w produkcji: WARNING i wyżej
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", # Format komunikatu
    handlers=[
        logging.StreamHandler(),              # konsola
        # logging.FileHandler("app.log")        # przesłanie do pliku
    ]
)


def main():
    while True:
        print("\n" + "=" * 60)
        print("TASK TRACKER")
        print("=" * 60)
        print("\nMENU GŁÓWNE")
        print("(1) ZALOGUJ SIĘ")
        print("(2) ZAREJESTRUJ SIĘ")
        print("(3) WYJDŹ")
        print("\nDEMO UŻYTKOWNIK: user1 / pass123 (Jan Kowalski)")

        choice = int(input("\nWybierz opcję: "))

        if choice == 1:
            user = login_screen()
            if user:
                user_panel(user)
        elif choice == 2:
            register_screen()
        elif choice == 3:
            clear_screen()
            print("Dziękujemy za skorzystanie z aplikacji.")
            break
        else:
            print("\n❌ Nieprawidłowa opcja.")
            input("\nNaciśnij Enter...")


if __name__ == "__main__":
    main()
import psycopg2
import psycopg2.errorcodes
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError, ProgrammingError, IntegrityError, InterfaceError, Error
import logging
from config import DB_CONFIG


logger = logging.getLogger(__name__)


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def execute(query: str, params: tuple = (), fetch: str = None) -> dict | list | int | None:
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, params)

        if fetch == "one":
            return cursor.fetchone()
        elif fetch == "all":
            return cursor.fetchall()

        conn.commit()
        return cursor.statusmessage

    except IntegrityError as e:
        if conn:
            conn.rollback()
        if e.pgcode == psycopg2.errorcodes.UNIQUE_VIOLATION:
            logger.warning(f"Duplikat rekordu: {e}")
            raise
        logger.error(f"Naruszenie więzów bazy danych: {e}")
        raise

    except ProgrammingError as e:
        if conn:
            conn.rollback()
        logger.error(f"Błąd SQL (sprawdź zapytanie): {e}")
        raise

    except OperationalError as e:
        if conn:
            conn.rollback()
        logger.error(f"Błąd operacyjny (serwer/sieć): {e}")
        raise

    except InterfaceError as e:
        logger.error(f"Błąd interfejsu połączenia: {e}")
        raise

    except Error as e:
        if conn:
            conn.rollback()
        logger.error(f"Nieoczekiwany błąd PostgreSQL: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if conn and not conn.closed:
            conn.close()
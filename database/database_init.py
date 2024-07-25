import os
from contextlib import closing

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection

from create_tables import CREATE_COMMANDS
from fixtures import INSERT_COMMANDS
from pathlib import Path

DOTENV_PATH = Path(__file__).resolve().parent.joinpath(".env")

load_dotenv(dotenv_path=DOTENV_PATH)


def create(db_connection: connection, commands: list[str]) -> None:
    with db_connection.cursor() as cursor:
        for cmd in commands:
            cursor.execute(cmd)
        db_connection.commit()


def main() -> None:
    try:
        with closing(psycopg2.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"))
        ) as connection:
            create(commands=CREATE_COMMANDS, db_connection=connection)
            create(commands=INSERT_COMMANDS, db_connection=connection)
    except Exception:
        print('Произошла ошибка.')
    else:
        print('Инициализация и заполнение базы выполнены успешно.')


if __name__ == "__main__":
    main()

import os
from typing import Iterable

import psycopg2
from psycopg2 import sql


db_connection = psycopg2.connect(
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)


def select_genres() -> dict[int, dict]:
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT id, title FROM genres;")

        objects = {}
        for row in cursor.fetchall():
            objects[row[0]] = dict(
                zip(("Идентификатор", "Название"), row)
            )
        return objects


def insert(obj_data: dict[str, int | str], table_name: str) -> None:
    keys = obj_data.keys()
    values = obj_data.values()

    with db_connection.cursor() as cursor:
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
                sql.Identifier(table_name),
                sql.SQL(", ").join(map(sql.Identifier, keys)),
                sql.SQL(", ").join(map(sql.Literal, values))
               )
        cursor.execute(query)
        db_connection.commit()


def select_books(available_only: bool = False) -> dict[int, dict]:
    with db_connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT
                books.id,
                books.title,
                books.author_first_name,
                books.author_last_name,
                books.isbn,
                books.takes_count,
                CASE WHEN books.is_available then 'Да' else 'Нет' END,
                genres.id as genre_id,
                genres.title
            FROM books
            JOIN genres ON genres.id = books.genre_id
            {"WHERE books.is_available" if available_only else ""}
        """)

        objects = {}
        for row in cursor.fetchall():
            objects[row[0]] = dict(
                zip(
                    (
                        "Идентификатор",
                        "Название",
                        "Имя автора",
                        "Фамилия автора",
                        "ISBN",
                        "Количество прочтений",
                        "Доступна к выдаче",
                        "Идентификатор жанра",
                        "Название жанра",
                    ),
                    row
                )
            )
        return objects


def select_debt_books() -> dict[int, dict]:
    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                book_takes.id,
                book_takes.date_taken,
                book_takes.planned_date_return,
                users.id,
                users.first_name,
                users.last_name,
                books.id,
                books.isbn,
                books.takes_count,
            FROM book_takes
            JOIN books ON book_takes.id = books.id
            JOIN users ON users.id = book_takes.user_id
        """)

        objects = {}
        for row in cursor.fetchall():
            objects[row[0]] = dict(
                zip(
                    (
                        "Идентификатор факта взятия",
                        "Название книги",
                        "Плановое время возврата книги",
                        "Идентификатор читающего",
                        "Имя читающего",
                        "Фамилия читающего",
                        "Идентификатор книги",
                        "ISBN книги",
                        "Количество взятий книги",
                    ),
                    row
                )
            )
        return objects


def select_users(no_debts_only: bool = False) -> dict[int, dict]:
    with db_connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT
                users.id,
                users.first_name,
                users.last_name,
                users.address_latitude,
                users.address_longitude,
                users.books_taken_count,
                users.last_visit
            FROM users
            {"WHERE users.books_taken_count = 0" if no_debts_only else ""}
        """)

        objects = {}
        for row in cursor.fetchall():
            objects[row[0]] = dict(
                zip(
                    (
                        "Идентификатор",
                        "Имя читателя",
                        "Фамилия читателя",
                        "Широта адреса читателя",
                        "Долгота адреса читателя",
                        "Количество не возвращенных книг",
                        "Дата последнего посещения",
                    ),
                    row
                )
            )
        return objects


def update(obj_data: dict[str, int | str], table_name: str, id: int):
    with db_connection.cursor() as cursor:
        params = [
            sql.SQL("{} = {}").format(
                sql.Identifier(key),
                sql.Literal(value)
            ) for key, value in obj_data.items()
        ]
        query = sql.SQL("UPDATE {} SET {} WHERE id = {};").format(
                sql.Identifier(table_name),
                sql.SQL(", ").join(params),
                sql.Literal(id)
               )
        cursor.execute(query)
        db_connection.commit()


def delete(table_name: str, id: int):
    with db_connection.cursor() as cursor:
        query = sql.SQL("DELETE FROM {} WHERE id = {};").format(
                sql.Identifier(table_name),
                sql.Literal(id)
               )
        cursor.execute(query)
        db_connection.commit()


def give_book(book_id: int, user_id: int, days_interval: int):
    with db_connection.cursor() as cursor:
        update_book_query = sql.SQL(
            """
            UPDATE {table}
            SET {is_available} = false, {takes_count} = {takes_count} + 1
            WHERE id = {book_id};
            """
        ).format(
            table=sql.Identifier("books"),
            is_available=sql.Identifier("is_available"),
            takes_count=sql.Identifier("takes_count"),
            book_id=sql.Literal(book_id)
        )

        update_user_query = sql.SQL(
            """
            UPDATE {table}
            SET
                {books_taken_count} = {books_taken_count} + 1,
                {last_visit} = current_timestamp
            WHERE id = {user_id};
            """
        ).format(
            table=sql.Identifier("users"),
            user_id=sql.Literal(user_id),
            last_visit=sql.Identifier("last_visit"),
            books_taken_count=sql.Identifier("books_taken_count")
        )

        insert_take_query = sql.SQL(
            """
            INSERT INTO {} ({})
            VALUES (
                {},
                {},
                current_timestamp,
                current_timestamp + '{} days'
            );
            """
        ).format(
            sql.Identifier("book_takes"),
            sql.SQL(", ").join(map(sql.Identifier, [
                "user_id",
                "book_id",
                "date_taken",
                "planned_date_return"
            ])),
            sql.Literal(user_id),
            sql.Literal(book_id),
            sql.Literal(days_interval)
        )

        for query in update_book_query, update_user_query, insert_take_query:
            cursor.execute(query)
        db_connection.commit()


def take_book(taken_id: int, book_id: int, user_id: int):
    with db_connection.cursor() as cursor:
        update_book_query = sql.SQL(
            """
            UPDATE {}
            SET {} = true
            WHERE id = {};
            """
        ).format(
            sql.Identifier("books"),
            sql.Identifier("is_available"),
            sql.Literal(book_id)
        )

        update_user_query = sql.SQL(
            """
            UPDATE {}
            SET {} = current_timestamp
            WHERE id = {};
            """
        ).format(
            sql.Identifier("users"),
            sql.Identifier("last_visit"),
            sql.Literal(user_id)
        )

        delete_take_query = sql.SQL(
            """
            DELETE FROM {} WHERE id = {};
            """
        ).format(
            sql.Identifier("book_takes"),
            sql.Literal(taken_id)
        )

        for query in update_book_query, update_user_query, delete_take_query:
            cursor.execute(query)
        db_connection.commit()


def run_report_query(query: str, returning_columns: Iterable[str]):
    with db_connection.cursor() as cursor:
        cursor.execute(query)

        objects = {}
        for row in cursor.fetchall():
            objects[row[0]] = dict(zip(returning_columns, row))
        return objects

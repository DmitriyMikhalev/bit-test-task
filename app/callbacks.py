from queries import (
    insert,
    update,
    delete,
    select_users,
    select_books,
    give_book,
    select_debt_books,
    take_book
)
from utils import write_to_file, request_user_data, request_book_data
from validators import models
from decorators import callback


@callback
def add_book_callback():
    book = request_book_data()
    insert(book.model_dump(), "books")


@callback
def update_book_callback():
    books = select_books()
    write_to_file(books)
    book_id = int(input(
        """Список книг выведен в файл, введите идентификатор
           изменяемой книги: """)
    )
    new_book = request_book_data()

    update(new_book.model_dump(), "books", book_id)


@callback
def delete_book_callback():
    books = select_books(available_only=True)
    write_to_file(books)

    book_id = int(input(
        """Список книг выведен в файл, введите
            идентификатор удаляемой книги: """)
    )
    if book_id not in books:
        raise Exception(f"Книги с id = {book_id} в БД нет.")

    delete("books", book_id)


@callback
def add_user_callback():
    user = request_user_data()
    insert(user.model_dump(), "users")


@callback
def update_user_callback():
    users = select_users()
    write_to_file(users)

    user_id = int(input(
        """Список читателей выведен в файл, введите
            идентификатор изменяемого читателя: """)
    )
    user = request_user_data()

    update(user.model_dump(), "users", user_id)


@callback
def delete_user_callback():
    users = select_users()
    write_to_file(users)

    user_id = int(input(
        """Список читателей выведен в файл, введите
            идентификатор удаляемого читателя: """)
    )
    if user_id not in users:
        raise Exception(f"Книги с id = {user_id} в БД нет.")

    delete("users", user_id)


@callback
def take_book_back_callback():
    books_taken = select_debt_books()
    write_to_file(books_taken)

    taken_id = int(input(
        """Список записей выдачи книг выведен в файл, введите
            идентификатор закрываемого факта взятия книги: """)
    )
    book = books_taken[taken_id]

    take_book(
        taken_id,
        book["Идентификатор книги"],
        book["Идентификатор читающего"]
    )


@callback
def give_book_callback():
    books = select_books(available_only=True)
    write_to_file(books)
    book_id = int(input(
        """Список доступных книг выведен в файл, введите
            идентификатор выдаваемой книги: """)
    )

    users = select_users()
    write_to_file(users)
    user_id = int(input(
        """Список читателей выведен в файл, введите идентификатор
            читателя, которому выдается книга: """)
    )

    days_interval = int(
        input("Введите количество дней, на которое выдается книга: ")
    )

    book_takes = models.BookTakeModel(
        user_id=user_id,
        book_id=book_id,
        days_interval=days_interval
    )

    give_book(**book_takes.model_dump())

from queries import (
    insert,
    update,
    delete,
    select_users,
    select_books,
    give_book,
    select_debt_books,
    take_book,
    run_report_query
)
from utils import (
    write_to_file,
    write_to_geojson_file,
    request_user_data,
    request_book_data
)
from validators import models
from decorators import callback
from reports import (
    REPORT_MESSAGE,
    REPORT_COUNT_OF_BOOKS,
    REPORT_COUNT_OF_READERS,
    REPORT_BOOKS_TAKEN_BY_USER,
    REPORT_BOOKS_IN_HANDS_BY_USER,
    REPORT_LAST_VISIT_BY_USER,
    REPORT_MOST_POPULAR_AUTHOR,
    REPORT_GENRES_TOP,
    REPORT_OVERDUED_TAKES,
    REPORT_GIVEN_BOOKS
)


report_callback = callback(REPORT_MESSAGE)


@callback()
def add_book_callback():
    book = request_book_data()
    insert(book.model_dump(), "books")


@callback()
def update_book_callback():
    books = select_books()
    write_to_file(books)
    book_id = int(
        input(
            "Список книг выведен в файл, введите идентификатор "
            "изменяемой книги: "
        )
    )
    new_book = request_book_data()

    update(new_book.model_dump(), "books", book_id)


@callback()
def delete_book_callback():
    books = select_books(available_only=True)
    write_to_file(books)

    book_id = int(
        input(
            "Список книг выведен в файл, введите "
            "идентификатор удаляемой книги: "
        )
    )
    if book_id not in books:
        raise Exception(f"Книги с id = {book_id} в БД нет.")

    delete("books", book_id)


@callback()
def add_user_callback():
    user = request_user_data()
    insert(user.model_dump(), "users")


@callback()
def update_user_callback():
    users = select_users()
    write_to_file(users)

    user_id = int(
        input(
            "Список читателей выведен в файл, введите "
            "идентификатор изменяемого читателя: "
        )
    )
    user = request_user_data()

    update(user.model_dump(), "users", user_id)


@callback()
def delete_user_callback():
    users = select_users()
    write_to_file(users)

    user_id = int(
        input(
            "Список читателей выведен в файл, введите "
            "идентификатор удаляемого читателя: "
        )
    )
    if user_id not in users:
        raise Exception(f"Книги с id = {user_id} в БД нет.")

    delete("users", user_id)


@callback()
def take_book_back_callback():
    books_taken = select_debt_books()
    write_to_file(books_taken)

    taken_id = int(
        input(
            "Список записей выдачи книг выведен в файл, введите "
            "идентификатор закрываемого факта взятия книги: "
        )
    )
    book = books_taken[taken_id]

    take_book(
        taken_id,
        book["Идентификатор книги"],
        book["Идентификатор читающего"]
    )


@callback()
def give_book_callback():
    books = select_books(available_only=True)
    write_to_file(books)
    book_id = int(
        input(
            "Список доступных книг выведен в файл, введите "
            "идентификатор выдаваемой книги: "
        )
    )

    users = select_users()
    write_to_file(users)
    user_id = int(
        input(
            "Список читателей выведен в файл, введите идентификатор "
            "читателя, которому выдается книга: "
        )
    )

    days_interval = int(
        input("Введите количество дней, на которое выдается книга: ")
    )

    book_takes = models.BookTakeModel(
        user_id=user_id,
        book_id=book_id,
        days_interval=days_interval
    )

    if book_id not in books:
        raise Exception("Книга недоступна к выдаче.")

    give_book(**book_takes.model_dump())


@report_callback
def show_books_callback():
    books = select_books()
    write_to_file(books)


@report_callback
def show_count_readers_books_callback():
    print(type(REPORT_COUNT_OF_BOOKS))
    books_count = run_report_query(
        REPORT_COUNT_OF_BOOKS,
        ("Количество книг",)
    )
    users_count = run_report_query(
        REPORT_COUNT_OF_READERS,
        ("Количество читателей",)
    )
    write_to_file(objs={**books_count, **users_count})


@report_callback
def show_taken_books_by_user_callback():
    books_by_user = run_report_query(
        REPORT_BOOKS_TAKEN_BY_USER,
        (
            "Идентификатор читателя",
            "Имя читателя",
            "Фамилия читателя",
            "Количество взятых за все время книг"
        )
    )
    write_to_file(books_by_user)


@report_callback
def show_count_in_hands_by_user_callback():
    books_in_hands = run_report_query(
        REPORT_BOOKS_IN_HANDS_BY_USER,
        (
            "Идентификатор читателя",
            "Имя читателя",
            "Фамилия читателя",
            "Книг на руках"
        )
    )
    write_to_file(books_in_hands)


@report_callback
def show_last_visist_by_user_callback():
    last_visits = run_report_query(
        REPORT_LAST_VISIT_BY_USER,
        (
            "Идентификатор читателя",
            "Имя читателя",
            "Фамилия читателя",
            "Дата последнего посещения"
        )
    )
    write_to_file(last_visits)


@report_callback
def show_most_popular_author_callback():
    author = run_report_query(
        REPORT_MOST_POPULAR_AUTHOR,
        (
            "Имя автора",
            "Фамилия автора",
            "Количество прочтений книг автора"
        )
    )
    write_to_file(author)


@report_callback
def show_genres_top_callback():
    genres = run_report_query(
        REPORT_GENRES_TOP,
        (
            "Название жанра",
            "Количество книг"
        )
    )
    write_to_file(genres)


@report_callback
def show_overdued_takes_callback():
    overdued_takes = run_report_query(
        REPORT_OVERDUED_TAKES,
        (
            "Идентификатор читателя",
            "Имя читателя",
            "Фамилия читателя",
            "Широта адреса читателя",
            "Долгота адреса читателя",
            "Идентификатор факта взятия книги",
            "Дата взятия книги",
            "Плановая дата возвращения книги",
            "Просроченное время",
            "Идентификатор книги",
            "ISBN",
            "Название книги"
        )
    )
    write_to_file(overdued_takes)


@callback(
    msg="\nОтчет загружен в файл .geojson, для просмотра данных на "
        "карте используйте, например, https://geojson.io/\n"
)
def show_given_books_on_map_callback():
    given_books = run_report_query(
        REPORT_GIVEN_BOOKS,
        (
            "Идентификатор читателя",
            "Имя читателя",
            "Фамилия читателя",
            "Широта адреса читателя",
            "Долгота адреса читателя",
            "Плановая дата возвращения книги",
            "Идентификатор книги",
            "ISBN",
            "Название книги"
        )
    )
    write_to_geojson_file(given_books)

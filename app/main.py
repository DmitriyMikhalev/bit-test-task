import logging
import logging.handlers

from callbacks import (
    add_book_callback,
    update_book_callback,
    delete_book_callback,
    add_user_callback,
    update_user_callback,
    delete_user_callback,
    take_book_back_callback,
    give_book_callback,
    show_books_callback,
    show_count_readers_books_callback,
    show_taken_books_by_user_callback,
    show_count_in_hands_by_user_callback,
    show_last_visist_by_user_callback,
    show_most_popular_author_callback,
    show_genres_top_callback,
    show_overdued_takes_callback,
    show_given_books_on_map_callback
)
from menu import option, menu, handler


logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

logger_handler = logging.FileHandler("log.log", encoding="utf-8")
logger_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}",
    style="{"
)
logger_handler.setFormatter(formatter)
logger.addHandler(logger_handler)

books_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption(
            "Добавить книгу;",
            add_book_callback
        ),
        option.FunctionalMenuOption(
            "Изменить книгу;",
            update_book_callback
        ),
        option.FunctionalMenuOption(
            "Удалить книгу;",
            delete_book_callback
        ),
    ]
)

users_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption(
            "Добавить читателя;",
            add_user_callback
        ),
        option.FunctionalMenuOption(
            "Изменить читателя;",
            update_user_callback
        ),
        option.FunctionalMenuOption(
            "Удалить читателя;",
            delete_user_callback
        ),
    ]
)

book_takes_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption(
            "Добавить факт взятия книги;",
            give_book_callback
        ),
        option.FunctionalMenuOption(
            "Добавить факт возвращения книги;",
            take_book_back_callback
        ),
    ]
)

reports_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption(
            "Список книг;",
            show_books_callback
        ),
        option.FunctionalMenuOption(
            "Количество читателей, книг;",
            show_count_readers_books_callback
        ),
        option.FunctionalMenuOption(
            "Сколько книг брал каждый читатель за все время;",
            show_taken_books_by_user_callback
        ),
        option.FunctionalMenuOption(
            "Сколько книг сейчас находится на руках у каждого читателя;",
            show_count_in_hands_by_user_callback
        ),
        option.FunctionalMenuOption(
            "Дата последнего посещения читателями библиотеки;",
            show_last_visist_by_user_callback
        ),
        option.FunctionalMenuOption(
            "Самый читаемый автор;",
            show_most_popular_author_callback
        ),
        option.FunctionalMenuOption(
            "Самый популярные жанры по убыванию;",
            show_genres_top_callback
        ),
        option.FunctionalMenuOption(
            "Информация о просроченных сдачах книг;",
            show_overdued_takes_callback
        ),
        option.FunctionalMenuOption(
            "Информация о выданных книгах на карте;",
            show_given_books_on_map_callback
        ),
    ]
)

main_menu = menu.Menu(
    options=[
        option.MenuOption("Манипулирование книгами;"),
        option.MenuOption("Манипулирование читателями;"),
        option.MenuOption("Манипулирование взятиями/возвращениями книг;"),
        option.MenuOption("Создание отчетов.")
    ],
    submenues=[books_menu, users_menu, book_takes_menu, reports_menu]
)

menu_handler = handler.MenuHandler(root_menu=main_menu)


def main(menu_handler: handler.MenuHandler = menu_handler) -> None:
    try:
        menu_handler.poll()
    except KeyboardInterrupt:
        from queries import db_connection
        db_connection.close()
        print("Выполнено принудительное завершение программы.")


if __name__ == "__main__":
    main()

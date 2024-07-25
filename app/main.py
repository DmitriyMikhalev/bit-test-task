from callbacks import (
    add_book_callback,
    update_book_callback,
    delete_book_callback,
    add_user_callback,
    update_user_callback,
    delete_user_callback,
    take_book_back_callback,
    give_book_callback
)
from menu import option, menu, handler


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

reports_menu = menu.Menu(
    options=[]
)

main_menu = menu.Menu(
    options=[
        option.MenuOption("Манипулирование книгами;"),
        option.MenuOption("Манипулирование читателями;"),
        option.MenuOption("Манипулирование взятиями/возвращениями книг;"),
    ],
    submenues=[books_menu, users_menu, book_takes_menu]
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

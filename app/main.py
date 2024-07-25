from menu import option, menu, handler


books_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption("Добавить книгу;", lambda: print('add book')),
        option.FunctionalMenuOption("Изменить книгу;", lambda: print('upd book')),
        option.FunctionalMenuOption("Удалить книгу;", lambda: print('del book')),
    ]
)
users_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption("Добавить читателя;", lambda: print('add user')),
        option.FunctionalMenuOption("Изменить читателя;", lambda: print('upd user')),
        option.FunctionalMenuOption("Удалить читателя;", lambda: print('del user')),
    ]
)
book_takes_menu = menu.FunctionalMenu(
    options=[
        option.FunctionalMenuOption("Добавить факт возвращения книги;", lambda: print('add took')),
        option.FunctionalMenuOption("Добавить факт взятия книги;", lambda: print('del took')),
    ]
)
reports_menu = menu.Menu(
    options=[]
)


main_menu = menu.Menu(
    options=[
        option.MenuOption("Манипулирование книгами;"),
        option.MenuOption("Манипулирование пользователями;"),
        option.MenuOption("Манипулирование взятиями/возвращениями книг;"),
    ],
    FunctionalMenues=[books_menu, users_menu, book_takes_menu]
)


menu_handler = handler.MenuHandler(root_menu=main_menu)


def main(menu_handler: handler.MenuHandler = menu_handler) -> None:
    try:
        menu_handler.poll()
    except KeyboardInterrupt:
        print('Выполнено принудительное завершение программы.')


if __name__ == "__main__":
    main()

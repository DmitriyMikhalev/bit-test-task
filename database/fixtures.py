INSERT_GENRES = [
    """INSERT INTO genres (title) VALUES ('Детектив');""",
    """INSERT INTO genres (title) VALUES ('Фантастика');""",
    """INSERT INTO genres (title) VALUES ('Приключения');""",
    """INSERT INTO genres (title) VALUES ('Роман');""",
    """INSERT INTO genres (title) VALUES ('Научная книга');""",
    """INSERT INTO genres (title) VALUES ('Фольклор');""",
    """INSERT INTO genres (title) VALUES ('Юмор');""",
    """INSERT INTO genres (title) VALUES ('Справочная книга');""",
    """INSERT INTO genres (title) VALUES ('Поэзия');""",
    """INSERT INTO genres (title) VALUES ('Детская книга');""",
    """INSERT INTO genres (title) VALUES ('Документальная литература');""",
    """INSERT INTO genres (title) VALUES ('Деловая литература');""",
    """INSERT INTO genres (title) VALUES ('Религиозная литература');""",
    """INSERT INTO genres (title) VALUES ('Учебная книга');""",
    """INSERT INTO genres (title) VALUES ('Психология');""",
    """INSERT INTO genres (title) VALUES ('Техника');""",
]


INSERT_USERS = [
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Егор',
        'Шишкин',
        56.25335580822062,
        57.99404682665673,
        '2024-07-20 10:00:00+05'
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Василий',
        'Сидоров',
        56.24033030496355,
        57.99613905459623,
        '2024-07-20 10:00:00+05'
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Егор',
        'Зимирев',
        56.2881771591681,
        57.999259451823946,
        '2024-07-20 10:00:00+05'
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit, books_taken_count) VALUES (
        'Алина',
        'Сотова',
        56.19174619716455,
        57.974766513304104,
        '2024-06-23 23:02:18.767979+05',
        1
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit, books_taken_count) VALUES (
        'Мария',
        'Хошина',
        56.2474268966329,
        57.99739033822749,
        '2024-03-13 13:00:00+05',
        1
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit, books_taken_count) VALUES (
        'Андрей',
        'Иванов',
        56.21712003835552,
        58.04959930832348,
        '2024-07-20 14:00:43+05',
        1
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Анна',
        'Бабина',
        56.16952418200728,
        57.998235353324986,
        '2024-07-20 10:00:00+05'
    );
    """
]

INSERT_BOOKS = [
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count, is_available) VALUES (
        'Изучаем Python Том 1 Издание 5', 'Марк', 'Лутц', '978-5-907144-52-1', 14, 17, false
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count, is_available) VALUES (
        'Изучаем Python Том 2 Издание 5', 'Марк', 'Лутц', '978-5-907144-53-8', 14, 10, false
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count) VALUES (
        'Asyncio и конкурентное программирование', 'Мэттью', 'Фаулер', '978-5-93700-166-5', 14, 2
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count) VALUES (
        'Мастер и Маргарита', 'Михаил', 'Булгаков', '978-5-17-112392-5', 4, 4
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count) VALUES (
        'Тропа войны', 'Майн', 'Рид', '978-5-4444-3810-7', 4, 1
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count) VALUES (
        'Теория всего', 'Стивен', 'Хокинг', '978-5-17-102340-9', 5, 12
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id, takes_count, is_available) VALUES (
        'Сборник цитат Стетхема', 'Константин', 'Беляков', '978-5-90-776903-8', 7, 26, false
    );"""
]

INSERT_BOOK_TAKES = [
    """
        INSERT INTO book_takes (user_id, book_id, date_taken, planned_date_return) VALUES (
            4, 1, '2024-06-23 23:02:18.767979+05', '2024-12-18 23:02:18.767979+05'
        );
    """,
    """
        INSERT INTO book_takes (user_id, book_id, date_taken, planned_date_return) VALUES (
            5, 7, '2024-03-13 13:00:00+05', '2024-04-13 13:00:00+05'
        );
    """,
    """
        INSERT INTO book_takes (user_id, book_id, date_taken, planned_date_return) VALUES (
            6, 2, '2024-07-20 14:00:43+05', '2024-07-21 14:00:43+05'
        );
    """
]


INSERT_COMMANDS = [
    *INSERT_GENRES,
    *INSERT_USERS,
    *INSERT_BOOKS,
    *INSERT_BOOK_TAKES
]

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
        DEFAULT
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Василий',
        'Сидоров',
        56.24033030496355,
        57.99613905459623,
        DEFAULT
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Егор',
        'Зимирев',
        56.2881771591681,
        57.999259451823946,
        DEFAULT
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Алина',
        'Сотова',
        56.19174619716455,
        57.974766513304104,
        DEFAULT
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Мария',
        'Хошина',
        56.2474268966329,
        57.99739033822749,
        DEFAULT

    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Андрей',
        'Иванов',
        56.21712003835552,
        58.04959930832348,
        DEFAULT
    );
    """,
    """
    INSERT INTO users (first_name, last_name, address_latitude, address_longitude, last_visit) VALUES (
        'Анна',
        'Бабина',
        56.16952418200728,
        57.998235353324986,
        DEFAULT
    );
    """
]

INSERT_BOOKS = [
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Изучаем Python Том 1 Издание 5', 'Марк', 'Лутц', '978-5-907144-52-1', 14
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Изучаем Python Том 2 Издание 5', 'Марк', 'Лутц', '978-5-907144-53-8', 14
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Asyncio и конкурентное программирование', 'Мэттью', 'Фаулер', '978-5-93700-166-5', 14
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Мастер и Маргарита', 'Михаил', 'Булгаков', '978-5-17-112392-5', 4
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Тропа войны', 'Майн', 'Рид', '978-5-4444-3810-7', 4
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Теория всего', 'Стивен', 'Хокинг', '978-5-17-102340-9', 5
    );""",
    """INSERT INTO books (title, author_first_name, author_last_name, isbn, genre_id) VALUES (
        'Сборник цитат Стетхема', 'Константин', 'Беляков', '978-5-90-776903-8', 7
    );"""
]

INSERT_COMMANDS = [*INSERT_GENRES, *INSERT_USERS, *INSERT_BOOKS]

import os

REPORT_PATH = os.getenv("OUTPUT_PATH", "report.txt")

REPORT_MESSAGE = ("\nОперация успешно завершена, отчет сохранен в "
                  f"файл {REPORT_PATH}.\n")

REPORT_COUNT_OF_READERS = """SELECT COUNT(*) FROM users;"""

REPORT_COUNT_OF_BOOKS = """SELECT COUNT(*) FROM books;"""

REPORT_BOOKS_TAKEN_BY_USER = """
    SELECT id, first_name, last_name, books_taken_count
    FROM users;
"""

REPORT_BOOKS_IN_HANDS_BY_USER = """
    SELECT
        users.id,
        users.first_name,
        users.last_name,
        COUNT(*) as books_in_hands
    FROM
        users
    JOIN book_takes ON book_takes.user_id = users.id
    GROUP BY users.id;
"""

REPORT_LAST_VISIT_BY_USER = """
    SELECT
        users.id,
        users.first_name,
        users.last_name,
        users.last_visit
    FROM users;
"""

REPORT_MOST_POPULAR_AUTHOR = """
    SELECT
        author_first_name,
        author_last_name,
        SUM(takes_count) AS reads_count
    FROM
        books
    GROUP BY
        author_first_name, author_last_name
    ORDER BY
        reads_count DESC
    LIMIT 1;
"""

REPORT_GENRES_TOP = """
    SELECT
        genres.title,
        COUNT(*) AS cnt
    FROM books
    JOIN genres ON genres.id = books.genre_id
    GROUP BY genres.title
    ORDER BY cnt DESC;
"""

REPORT_OVERDUED_TAKES = """
    SELECT
        users.id as user_id,
        users.first_name,
        users.last_name,
        users.address_latitude,
        users.address_longitude,
        book_takes.id AS take_id,
        book_takes.date_taken,
        book_takes.planned_date_return,
        current_timestamp - book_takes.planned_date_return AS overuded_days,
        books.id as book_id,
        books.isbn,
        books.title
    FROM book_takes
    JOIN books ON books.id = book_takes.book_id
    JOIN users ON users.id = book_takes.user_id
    WHERE book_takes.id IN (SELECT id FROM book_takes WHERE planned_date_return < current_timestamp);
"""

REPORT_GIVEN_BOOKS = """
    SELECT
        users.id as user_id,
        users.first_name,
        users.last_name,
        users.address_latitude,
        users.address_longitude,
        book_takes.planned_date_return,
        books.id as book_id,
        books.isbn,
        books.title
    FROM book_takes
    JOIN books ON books.id = book_takes.book_id
    JOIN users ON users.id = book_takes.user_id;
"""

CREATE_TABLE_GENRE = """
    CREATE TABLE IF NOT EXISTS genres (
        id SERIAL PRIMARY KEY,
        title VARCHAR NOT NULL UNIQUE
    );
"""

CREATE_TABLE_BOOKS = """
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR NOT NULL,
        author_first_name VARCHAR NOT NULL,
        author_last_name VARCHAR NOT NULL,
        isbn VARCHAR NOT NULL UNIQUE,
        is_available BOOLEAN NOT NULL DEFAULT true,
        genre_id INTEGER NOT NULL,
        FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE RESTRICT,
        CONSTRAINT unique_author_book UNIQUE(title, author_first_name, author_last_name)
    );
"""

CREATE_TABLE_USERS = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        address_latitude NUMERIC(16, 14) NOT NULL CHECK(address_latitude >= -90 AND address_latitude <= 90),
        address_longitude NUMERIC(17, 14) NOT NULL CHECK(address_longitude >= -180 AND address_longitude < 180),
        books_taken_count INTEGER NOT NULL CHECK(books_taken_count >= 0) DEFAULT 0,
        last_visit TIMESTAMPTZ NOT NULL DEFAULT current_timestamp
    );
"""

CREATE_TABLE_BOOK_TAKES = """
    CREATE TABLE IF NOT EXISTS book_takes (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        date_taken TIMESTAMPTZ NOT NULL,
        PLANNED_DATE_RETURN TIMESTAMPTZ NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT,
        FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE RESTRICT
    );
"""

CREATE_COMMANDS = [CREATE_TABLE_GENRE, CREATE_TABLE_USERS, CREATE_TABLE_BOOKS, CREATE_TABLE_BOOK_TAKES]

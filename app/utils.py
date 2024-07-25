import os
from typing import Iterable
from pathlib import Path

from dotenv import load_dotenv

from queries import select_genres
from validators.models import UserModel, BookModel


DOTENV_PATH = Path(__file__).resolve().parent.parent.joinpath(".env")

load_dotenv(dotenv_path=DOTENV_PATH)

OUTPUT_PATH = os.getenv("OUTPUT_PATH")


def convert_obj_to_str(obj: dict[int, dict]) -> str:
    return "\n".join(f"{key}: {value}" for key, value in obj.items())


def write_to_file(objs: Iterable[dict]) -> None:
    obj_representations: list[str] = [
        convert_obj_to_str(obj) + "\n\n" for obj in objs.values()
    ]
    with open(OUTPUT_PATH, mode="w", encoding="utf-8") as file:
        file.writelines(obj_representations)


def request_user_data() -> UserModel:
    user_data = {
        "first_name": input("Введите имя читателя: ").strip(),
        "last_name": input("Введите фамилию читателя: ").strip(),
        "address_latitude": input("Введите широту адреса читателя: ").strip(),
        "address_longitude": input("Введите долготу адреса читателя: ").strip()
    }

    return UserModel(**user_data)


def request_book_data() -> BookModel:
    new_book_data = {
        "title": input("Введите название книги: ").strip(),
        "author_first_name": input("Введите имя автора книги: ").strip(),
        "author_last_name": input("Введите фамилию автора книги: ").strip(),
        "isbn": input("Введите код ISBN: ").strip()
    }

    genres = select_genres()
    write_to_file(genres)
    new_book_data["genre_id"] = input(
        "Список жанров выведен в файл, введите идентификатор жанра: "
    ).strip()

    return BookModel(**new_book_data)

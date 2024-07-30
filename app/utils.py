import os
import simplejson
from typing import Iterable
from pathlib import Path

from queries import select_genres
from validators.models import UserModel, BookModel


OUTPUT_PATH = os.getenv("OUTPUT_PATH")
GEOJSON_PATH = os.getenv("GEOJSON_PATH")


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


def convert_dict_to_geojson(objs: dict[int, dict]) -> dict:
    features = []
    for obj in objs.values():
        latitude = obj.pop("Широта адреса читателя")
        longitude = obj.pop("Долгота адреса читателя")

        features.append({
            "type": "Feature",
            "properties": obj,
            "geometry": {
                "coordinates": [latitude, longitude],
                "type": "Point"
            },
        })

    return {
        "type": "FeatureCollection",
        "features": features
    }


def write_to_geojson_file(objs: Iterable[dict]) -> None:
    objs = convert_dict_to_geojson(objs)
    with open(GEOJSON_PATH, mode="w", encoding="utf-8") as file:
        simplejson.dump(
            obj=objs,
            fp=file,
            indent=4,
            default=str,
            ensure_ascii=False,
            encoding="utf-8"
        )

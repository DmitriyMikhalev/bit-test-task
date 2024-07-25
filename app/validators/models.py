from pydantic import BaseModel, Field
from pydantic.types import PositiveInt
from pydantic_extra_types.coordinate import Latitude, Longitude


class UserModel(BaseModel):
    first_name: str
    last_name: str
    address_latitude: Latitude
    address_longitude: Longitude


class GenreModel(BaseModel):
    title: str


class BookModel(BaseModel):
    title: str
    author_first_name: str
    author_last_name: str
    isbn: str = Field(pattern=r"^978(?:-?\d){10}$")
    genre_id: PositiveInt


class BookTakeModel(BaseModel):
    user_id: PositiveInt
    book_id: PositiveInt
    days_interval: PositiveInt

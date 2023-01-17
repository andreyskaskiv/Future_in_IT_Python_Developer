from typing import NamedTuple
from typing import Callable


class Identification(NamedTuple):
    username: str
    password: str
    token: str


class Filenames(NamedTuple):
    year: int
    sex: str


class Name(NamedTuple):
    name: str
    qty_name: int


class Gender(NamedTuple):
    Boys: str
    Girls: str


class Args(NamedTuple):
    function: Callable
    gender: str
    quantity: int
    show_all_names: bool




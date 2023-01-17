from typing import NamedTuple


class DriverCompany(NamedTuple):
    driver: str
    company: str


class InfoTable(NamedTuple):
    counter: int
    driver: str
    company: str
    race_time: str

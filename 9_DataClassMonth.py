# Month can be created using dataclasses, but it's more
# complicated than using Enum with questionable benefits.
from dataclasses import dataclass, field
from typing import List
from check import check


@dataclass(frozen=True)
class Day:
    n: int

    def __post_init__(self) -> None:
        check(0 < self.n <= 31, f"Day({self.n}) out of range")


@dataclass(frozen=True)
class Year:
    n: int

    def __post_init__(self) -> None:
        check(1900 < self.n <= 2022, f"Year({self.n}) out of range")


@dataclass(frozen=True)
class Month:
    name: str
    n: int
    max_days: int

    def __post_init__(self):
        check(0 < self.n <= 12, f"Month({self.n}) out of range")
        check(self.max_days in [28, 30, 31], f"Month max_days {self.max_days} out of range")

    def check_day(self, day: Day):
        check(day.n <= self.max_days, f"{day} out of range for {self}")

    @staticmethod
    def make_months():
        return [Month(m[0], m[1], m[2]) for m in [
            ("January", 1, 31),
            ("February", 2, 28),
            ("March", 3, 31),
            ("April", 4, 30),
            ("May", 5, 31),
            ("June", 6, 30),
            ("July", 7, 31),
            ("August", 8, 31),
            ("September", 9, 30),
            ("October", 10, 31),
            ("November", 11, 30),
            ("December", 12, 31),
        ]]


@dataclass(frozen=True)
class Months:
    months: List[Month] = field(default_factory=Month.make_months)

    def number(self, month_number: int):
        check(0 < month_number <= 12, f"Month({month_number}) out of range")
        return self.months[month_number - 1]


@dataclass(frozen=True)
class BirthDate:
    m: Month
    d: Day
    y: Year

    def __post_init__(self):
        self.m.check_day(self.d)


if __name__ == '__main__':
    months = Months()
    for date in [
        (7, 8, 1957),
        (0, 32, 1857),
        (2, 31, 2022),
        (9, 31, 2022),
        (4, 31, 2022),
        (6, 31, 2022),
        (11, 31, 2022),
        (12, 31, 2022),
    ]:
        print(date)
        print(BirthDate(months.number(date[0]), Day(date[1]), Year(date[2])))
        print('-' * 30)

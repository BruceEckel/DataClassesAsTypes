# An Enum is also a type, and is preferable
# when you have a smaller set of values.
from dataclasses import dataclass
from enum import Enum
from check import check


@dataclass(frozen=True)
class Day:
    n: int

    def __post_init__(self) -> None:
        check(0 < self.n <= 31, f"{self.n}: Day of month out of range")


@dataclass(frozen=True)
class Year:
    n: int

    def __post_init__(self) -> None:
        check(1900 < self.n <= 2022, f"{self.n}: Year out of range")


class Month(Enum):
    JANUARY = (1, 31)
    FEBRUARY = (2, 28)
    MARCH = (3, 31)
    APRIL = (4, 30)
    MAY = (5, 31)
    JUNE = (6, 30)
    JULY = (7, 31)
    AUGUST = (8, 31)
    SEPTEMBER = (9, 30)
    OCTOBER = (10, 31)
    NOVEMBER = (11, 30)
    DECEMBER = (12, 31)

    @staticmethod
    def number(month_number: int):
        check(0 < month_number <= 12, f"Month {month_number} out of range")
        return list(Month)[month_number - 1]

    def check_day(self, day: Day):
        check(day.n <= self.value[1], f"{day} out of range for {self}")

    def __repr__(self):
        return self.name


@dataclass(frozen=True)
class BirthDate:
    m: Month
    d: Day
    y: Year

    def __post_init__(self):
        self.m.check_day(self.d)


if __name__ == '__main__':
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
        print(BirthDate(Month.number(date[0]), Day(date[1]), Year(date[2])))
        print('-' * 30)

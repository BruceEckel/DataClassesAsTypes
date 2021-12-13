from dataclasses import dataclass
from check import check

@dataclass(frozen=True)
class Day:
    day: int
    def __post_init__(self):
        check(0 < self.day <= 31, f"{self.day}: day of month out of range")

@dataclass(frozen=True)
class Month:
    month: int
    def __post_init__(self):
        check(0 < self.month <= 12, f"{self.month}: month out of range")

@dataclass(frozen=True)
class Year:
    year: int
    def __post_init__(self):
        check(1900 < self.year <= 2022, f"{self.year}: year out of range")

@dataclass(frozen=True)
class BirthDate:
    m: Month
    d: Day
    y: Year

if __name__ == '__main__':
    print(BirthDate(Month(7), Day(8), Year(1957)))
    print(BirthDate(Month(0), Day(32), Year(1857)))

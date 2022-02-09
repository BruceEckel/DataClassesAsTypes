from dataclasses import dataclass
from check import check

@dataclass(frozen=True)
class Day:
    day: int
    def __post_init__(self) -> None:
        check(0 < self.day <= 31, f"{self.day}: day of month out of range")

@dataclass(frozen=True)
class Month:
    month: int
    def __post_init__(self) -> None:
        check(1 <= self.month <= 12, f"{self.month}: month out of range")

@dataclass(frozen=True)
class MonthDay:
    month: Month
    day: Day
    def __post_init__(self) -> None:
        """
        30 days has September, April, June and November
        All the rest have 31
        Except February, which stands alone with 28
        """
        print(f"self.month.month: {self.month.month}")
        print(f"self.day.day: {self.day.day}")
        match self.month.month:
            case 2:
                print("case [2]")
                check(self.day.day <= 28,
                      f"MonthDay: {self.day} out of range for {self.month}")
            case 9 | 4 | 6 | 11:
                print("case [9, 4, 6, 11]")
                check(self.day.day <= 30,
                    f"MonthDay: {self.day} out of range for {self.month}")
            case _:
                print("case _")
                check(self.day.day <= 31,
                    f"MonthDay: {self.day} out of range for {self.month}")

@dataclass(frozen=True)
class Year:
    year: int
    def __post_init__(self) -> None:
        check(1900 < self.year <= 2022, f"{self.year}: year out of range")

@dataclass(frozen=True)
class BirthDate:
    m: Month
    d: Day
    y: Year

if __name__ == '__main__':
    print(BirthDate(Month(7), Day(8), Year(1957)))
    print(BirthDate(Month(0), Day(32), Year(1857)))
    print(MonthDay(Month(9), Day(31)))

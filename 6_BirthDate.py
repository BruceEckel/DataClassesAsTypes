from dataclasses import dataclass
from check import check

def trace(self): print(f"{self} __post_init__")

@dataclass(frozen=True)
class Day:
    day: int
    def __repr__(self):
        return f"Day({self.day})"
    def __post_init__(self) -> None:
        trace(self)
        check(0 < self.day <= 31, f"{self.day}: day of month out of range")

@dataclass(frozen=True)
class Month:
    month: int
    def __repr__(self):
        return f"Month({self.month})"
    def __post_init__(self) -> None:
        trace(self)
        check(1 <= self.month <= 12, f"{self.month}: month out of range")

@dataclass(frozen=True)
class Year:
    year: int
    def __repr__(self):
        return f"Year({self.year})"
    def __post_init__(self) -> None:
        trace(self)
        check(1900 < self.year <= 2022, f"{self.year}: year out of range")

@dataclass(frozen=True)
class BirthDate:
    m: Month
    d: Day
    y: Year
    def max_days(self, max_day):
        print(f"Checking max_days({max_day})")
        check(self.d.day <= max_day,
              f"MonthDay: {self.d} out of range for {self.m}")
    def __post_init__(self) -> None:
        trace(self)
        match self.m:
            case Month(2):  # February
                print("case Month(2)")
                self.max_days(28)
            case Month(9 | 4 | 6 | 11):  # September, April, June and November
                print("case Month(9 | 4 | 6 | 11)")
                self.max_days(30)
            case Month(_):  # All the rest...
                print("case Month(_)")
                self.max_days(31)
        print('-' * 30)

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
        BirthDate(Month(date[0]), Day(date[1]), Year(date[2]))

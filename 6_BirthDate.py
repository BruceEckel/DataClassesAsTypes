from dataclasses import dataclass
from check import check

@dataclass(frozen=True)
class Day:
    day: int
    def __repr__(self):
        return f"Day({self.day})"
    def __post_init__(self) -> None:
        print(f"{self} __post_init__")
        check(0 < self.day <= 31, f"{self.day}: day of month out of range")

@dataclass(frozen=True)
class Month:
    month: int
    def __repr__(self):
        return f"Month({self.month})"
    def __post_init__(self) -> None:
        print(f"{self} __post_init__")
        check(1 <= self.month <= 12, f"{self.month}: month out of range")

# @dataclass(frozen=True)
# class MonthDay:
#     month: Month
#     day: Day
#     def __repr__(self):
#         return f"MonthDay({self.month}, {self.day})"
#     def validate(self, max_day):
#         check(self.day.day <= max_day,
#               f"MonthDay: {self.day} out of range for {self.month}")
#     def __post_init__(self) -> None:
#         """
#         30 days has September, April, June and November
#         All the rest have 31
#         Except February, which stands alone with 28
#         """
#         print(self)
#         match self.month:
#             case Month(2):
#                 print("case Month(2)")
#                 self.validate(28)
#             case Month(9 | 4 | 6 | 11):
#                 print("case Month(9 | 4 | 6 | 11)")
#                 self.validate(30)
#             case _:
#                 print("case _")
#                 self.validate(31)

@dataclass(frozen=True)
class Year:
    year: int
    def __repr__(self):
        return f"Year({self.year})"
    def __post_init__(self) -> None:
        print(f"{self} __post_init__")
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
        print(f"{self} __post_init__")
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
    BirthDate(Month(7), Day(8), Year(1957))
    BirthDate(Month(0), Day(32), Year(1857))
    BirthDate(Month(2), Day(31), Year(2022))
    BirthDate(Month(9), Day(31), Year(2022))
    BirthDate(Month(4), Day(31), Year(2022))
    BirthDate(Month(6), Day(31), Year(2022))
    BirthDate(Month(11), Day(31), Year(2022))
    BirthDate(Month(12), Day(31), Year(2022))


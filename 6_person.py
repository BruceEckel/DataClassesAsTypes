# Composing a dataclass from other dataclasses
from dataclasses import dataclass
from validation import check

@dataclass(frozen=True)
class FullName:
    name: str
    def __post_init__(self) -> None:
        print(f"FullName checking {self.name}")
        check(len(self.name.split()) > 1,
              f"'{self.name}'",
              "needs at least first and last names")

@dataclass(frozen=True)
class BirthDate:
    dob: str
    def __post_init__(self) -> None:
        print(f"BirthDate checking {self.dob}")

@dataclass(frozen=True)
class EmailAddress:
    address: str
    def __post_init__(self) -> None:
        print(f"EmailAddress checking {self.address}")

@dataclass(frozen=True)
class Person:
    name: FullName
    date_of_birth: BirthDate
    email: EmailAddress

if __name__ == '__main__':
    person = Person(
        FullName("Bruce Eckel"),
        BirthDate("7/8/1957"),
        EmailAddress("mindviewinc@gmail.com")
    )
    print(person)

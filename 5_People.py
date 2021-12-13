from dataclasses import dataclass
from check import check

@dataclass(frozen=True)
class FullName:
    name: str
    def __post_init__(self):
        print(f"FullName checking {self.name}")
        check(len(self.name.split()) > 1,
              f"'{self.name}' needs at least first and last names")


@dataclass(frozen=True)
class BirthDate:
    dob: str
    def __post_init__(self):
        print(f"BirthDate checking {self.dob}")
        check(True, f"Add code to validate {self.dob}")


@dataclass(frozen=True)
class EmailAddress:
    address: str
    def __post_init__(self):
        print(f"EmailAddress checking {self.address}")
        check(True, f"Add code to validate {self.address}")


@dataclass(frozen=True)
class Person:
    name: FullName
    date_of_birth: BirthDate
    email: EmailAddress
    def __post_init__(self):
        print(f"Person checking fields")
        check(True, f"Add code to validate Person")


if __name__ == '__main__':
    person = Person(
        FullName("Bruce Eckel"),
        BirthDate("7/8/1957"),
        EmailAddress("mindviewinc@gmail.com")
    )

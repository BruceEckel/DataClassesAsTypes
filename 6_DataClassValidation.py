# "Make impossible values unrepresentable"
from dataclasses import dataclass
from check import check

@dataclass(frozen=True)
class Stars:
    number: int
    def __post_init__(self) -> None:
        check(0 < self.number <= 10, f"{self.number} out of range")

def f1(s: Stars) -> Stars:
    return Stars(s.number * 10)

def f2(s: Stars) -> Stars:
    return Stars(s.number + 10)

if __name__ == '__main__':
    stars1 = Stars(6)
    print(stars1)
    print(f1(stars1))
    print(f2(stars1))
    stars2 = Stars(11)
    print(f1(stars2))
    # stars1.number = 99  # Can't modify number

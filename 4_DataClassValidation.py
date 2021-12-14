from dataclasses import dataclass
from check import check

@dataclass(frozen=True)
class OneToTen:
    val: int
    def __post_init__(self) -> None:
        check(0 < self.val <= 10, f"{self.val} out of range")

def f1(x: OneToTen) -> OneToTen:
    return OneToTen(x.val * 10)

def f2(x: OneToTen) -> OneToTen:
    return OneToTen(x.val + 10)

if __name__ == '__main__':
    a = OneToTen(6)
    print(a)
    print(f1(a))
    print(f2(a))
    b = OneToTen(11)
    print(f1(b))
    # a.val = 99  # Can't modify val

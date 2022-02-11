# Careful encapsulation
from check import check


class Stars:
    def __init__(self, number: int):
        self._number = number
        check(0 < self._number <= 10, f"{self}")

    # Must remember to prevent modification:
    @property
    def number(self): return self._number

    # Create readable output:
    def __str__(self) -> str:
        return f"Stars({self.number})"


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
    # @property without setter prevents mutation:
    # stars1.number = 99
    # AttributeError: can't set attribute 'number'

# "A class is not a type"
from validation import check

class Stars:
    def condition(self, s: int = None):
        if s:
            check(0 < s <= 10, f"{self}: {s}")
        else:
            check(0 < self._number <= 10, f"{self}")

    def __init__(self, n_stars: int):
        self._number = n_stars
        self.condition()

    # Prevent external modification:
    @property
    def number(self): return self._number

    # Create readable output:
    def __str__(self) -> str:
        return f"Stars({self._number})"

    # Member functions guard the private variables:
    def f1(self, n_stars: int) -> int:
        self.condition(n_stars)  # Precondition
        self._number = n_stars + 5
        self.condition()  # Postcondition
        return self._number

    def f2(self, n_stars: int) -> int:
        self.condition(n_stars)  # Precondition
        self._number = n_stars * 5
        self.condition()  # Postcondition
        return self._number

if __name__ == '__main__':
    stars1 = Stars(4)
    print(stars1)
    print(stars1.f1(3))
    print(stars1.f2(stars1.f1(3)))
    stars2 = Stars(11)
    print(stars2.f1(2))
    print(stars2.f2(22))
    # @property without setter prevents mutation:
    # stars1.number = 99
    # AttributeError: can't set attribute 'number'

# "A class is not a type"
from check import check

class Stars:
    def __init__(self, number: int):
        self.number = number
    def __str__(self) -> str:
        return f"Stars({self.number})"

def f1(s: Stars) -> Stars:
    check(0 < s.number <= 10, f"{s.number} out of range")
    return Stars(s.number * 10)

def f2(s: Stars) -> Stars:
    check(0 < s.number <= 10, f"{s.number} out of range")
    return Stars(s.number + 10)

if __name__ == '__main__':
    stars1 = Stars(6)
    print(stars1)
    print(f1(stars1))
    print(f2(stars1))
    stars2 = Stars(11)
    print(f1(stars2))
    stars1.number = 99
    print(f2(stars1))

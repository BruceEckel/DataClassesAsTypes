from check import check

class Stars:
    def __init__(self, number: int):
        self.number = number
        check(0 < self.number <= 10, f"{self.number} out of range")
    def __str__(self) -> str:
        return f"Stars({self.number})"

def f1(x: Stars) -> Stars:
    return Stars(x.number * 10)

def f2(x: Stars) -> Stars:
    return Stars(x.number + 10)

if __name__ == '__main__':
    stars1 = Stars(6)
    print(stars1)
    print(f1(stars1))
    print(f2(stars1))
    stars2 = Stars(11)
    print(f1(stars2))
    stars1.number = 99   # Can still mutate to an invalid Stars
    print(stars1, "Didn't detect that it's out of range!")
    # So, still need to validate Stars inside functions
    print(f2(stars1))

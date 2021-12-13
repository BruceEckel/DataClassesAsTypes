from check import check

class OneToTen:
    def __init__(self, val: int):
        self.val = val
        check(0 < self.val <= 10, f"{self.val} out of range")
    def __str__(self):
        return f"OneToTen({self.val})"

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
    a.val = 99   # Can still mutate to an invalid OneToTen
    # Still need to validate OnToTen inside functions!
    print(f2(a))

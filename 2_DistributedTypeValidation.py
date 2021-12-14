from check import check

class OneToTen:
    def __init__(self, val: int):
        self.val = val
    def __str__(self) -> str:
        return f"OneToTen({self.val})"

def f1(x: OneToTen) -> OneToTen:
    check(0 < x.val <= 10, f"{x.val} out of range")
    return OneToTen(x.val * 10)

def f2(x: OneToTen) -> OneToTen:
    check(0 < x.val <= 10, f"{x.val} out of range")
    return OneToTen(x.val + 10)

if __name__ == '__main__':
    a = OneToTen(6)
    print(a)
    print(f1(a))
    print(f2(a))
    b = OneToTen(11)
    print(f1(b))
    a.val = 99
    print(f2(a))

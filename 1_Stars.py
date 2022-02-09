from check import check

def f1(stars: int) -> int:
    check(0 < stars <= 10, f"{stars} out of range")
    return stars * 10

def f2(stars: int) -> int:
    check(0 < stars <= 10, f"{stars} out of range")
    return stars + 10

if __name__ == '__main__':
    stars1 = 6
    print(stars1)
    print(f1(stars1))
    print(f2(stars1))
    stars2 = 11
    print(f1(stars2))
    stars1 = 99
    print(f2(stars1))
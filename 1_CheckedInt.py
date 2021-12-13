from check import check

def f1(one_to_ten: int) -> int:
    check(0 < one_to_ten <= 10, f"{one_to_ten} out of range")
    return one_to_ten * 10

def f2(one_to_ten: int) -> int:
    check(0 < one_to_ten <= 10, f"{one_to_ten} out of range")
    return one_to_ten + 10

if __name__ == '__main__':
    a = 6
    print(a)
    print(f1(a))
    print(f2(a))
    b = 11
    print(f1(b))
    a = 99
    print(f2(a))

from dataclasses import *
from enum import Enum


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class C:
    mylist: list[Point]


p = Point(10, 20)
print(p)
print(asdict(p))
print(astuple(p))

c = C([Point(2, 7), Point(10, 4)])
print(c)
print(asdict(c))
print(astuple(c))

p2 = replace(p, x=1, y=3)
p3 = replace(p, y=9)
p4 = replace(p3, x=-3)
for pn in [p, p2, p3, p4]:
    print(pn)
print(is_dataclass(c))


@dataclass
class Triple:
    x: float
    _: KW_ONLY  # After this point, all args must be provided in keyword form
    y: float
    z: float


t = Triple(0, y=1.5, z=2.0)
print(t)


@dataclass
class Rectangle:
    height: float
    width: float


@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        print(self)
        super().__init__(self.side, self.side)


square = Square(99.0, 88.0, 5.0)
print(square)

# You can assign any object to an enum value:

@dataclass
class Bar:
    ding: int
    dong: str

class Foo(Enum):
    BOO = Bar(1, "x")
    BE =  Bar(2, "y")
    DO =  Bar(3, "z")

print(Foo.DO.value.dong)

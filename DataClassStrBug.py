from dataclasses import dataclass

@dataclass
class Plumbus:
    size: int
    def __repr__(self):
        return f"!Plumbus({self.size})"

class Teacup:
    def __init__(self, capacity: int):
        self.capacity = capacity
    def __repr__(self):
        return f"!Teacup({self.capacity})"

@dataclass
class Frobnitz:
    plumbus: Plumbus
    teacup: Teacup
    def __repr__(self):
        return f"!Frobnitz({self.plumbus}, {self.teacup})"

if __name__ == '__main__':
    print(Frobnitz(Plumbus(42), Teacup(12)))

# Expected:
# Frobnitz(plumbus=!Plumbus(42), Teacup(12)
# Actual:
# Frobnitz(plumbus=Plumbus(size=42), teacup=<__main__.Teacup object at 0x000002C8C5157C10>)
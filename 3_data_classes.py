from dataclasses import dataclass, replace

@dataclass
class Messenger:
    name: str
    number: int
    depth: float = 0.0  # Default argument

if __name__ == '__main__':
    x = Messenger(name="x", number=9, depth=2.0)
    m = Messenger("foo", 12, 3.14)
    print(m)
    print(m.name, m.number, m.depth)
    mm = Messenger("xx", 1)  # Uses default argument
    print(mm == Messenger("xx", 1))  # Generates __eq__()
    print(mm == Messenger("xx", 2))

    # Make a copy with a different depth:
    mc = replace(m, depth=9.9)
    print(m, mc)

    # Mutable:
    m.name = "bar"
    print(m)
    # d = {m: "value"}
    # TypeError: unhashable type: 'Messenger'

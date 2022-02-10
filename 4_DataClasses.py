from dataclasses import dataclass

@dataclass
class Messenger:
    name: str
    number: int
    depth: float = 0.0  # Default

if __name__ == '__main__':
    m = Messenger("foo", 12, 3.14)
    print(m)
    print(m.number, m.name, m.depth)
    mm = Messenger("xx", 1)  # Uses default argument
    print(mm == Messenger("xx", 1))
    print(mm == Messenger("xx", 2))

    # Default dataclass is mutable:
    m.name = "bar"
    print(m)
    # d = {m: "value"}
    # TypeError: unhashable type: 'Messenger'

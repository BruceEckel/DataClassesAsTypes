from dataclasses import dataclass

@dataclass(frozen=True)
class Messenger:
    name: str
    number: int
    depth: float = 0.0  # Default

if __name__ == '__main__':
    m = Messenger("foo", 12, 3.14)
    print(m)
    # Frozen dataclass is immutable:
    # m.name = "bar"
    # dataclasses.FrozenInstanceError: cannot assign to field 'name'
    # Automatically creates __hash__():
    d = {m: "value"}
    print(d[m])

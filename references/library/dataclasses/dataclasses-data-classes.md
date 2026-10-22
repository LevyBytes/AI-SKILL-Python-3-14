# dataclasses — `dataclasses` — Data Classes

### `dataclasses` — Data Classes

**Source code:** [Lib/dataclasses.py](https://github.com/python/cpython/tree/3.14/Lib/dataclasses.py)

---

This module supplies a decorator together with functions that automatically attach generated [special methods](https://docs.python.org/3.14/glossary.html#term-special-method) — for instance [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) and [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) — onto classes the user writes. The original specification appeared in [**PEP 557**](https://peps.python.org/pep-0557/).

You declare the member variables that feed those generated methods through [**PEP 526**](https://peps.python.org/pep-0526/) type annotations. Consider this snippet:

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

```

Among other additions, it produces a `__init__()` resembling:

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand

```

Observe that this method gets attached to the class on its own: nothing in the `InventoryItem` definition above writes it out explicitly.

Added in version 3.7.

[Subject index](INDEX.md) · [Continue](module-contents-signature-and-initial-contract.md)

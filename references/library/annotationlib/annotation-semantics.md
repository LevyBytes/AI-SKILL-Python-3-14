# annotationlib - Annotation semantics

### Annotation semantics

How annotations get evaluated has shifted across the lifespan of Python 3, and at present it still hinges on a [future import](https://docs.python.org/3.14/reference/simple_stmts.html#future). The following execution models have existed for annotations:

- *Stock semantics* (the default from Python 3.0 up through 3.13; refer to [**PEP 3107**](https://peps.python.org/pep-3107/) and [**PEP 526**](https://peps.python.org/pep-0526/)): annotations get evaluated eagerly, the moment they are met in the source.

- *Stringified annotations* (engaged via `from __future__ import annotations` starting in Python 3.7; refer to [**PEP 563**](https://peps.python.org/pep-0563/)): annotations are kept purely as strings.

- *Deferred evaluation* (the default beginning in Python 3.14; refer to [**PEP 649**](https://peps.python.org/pep-0649/) and [**PEP 749**](https://peps.python.org/pep-0749/)): annotations get evaluated lazily, taking effect only at the point where they are accessed.

For instance, take the program below:

```python
def func(a: Cls) -> None:
    print(a)

class Cls: pass

print(func.__annotations__)

```

Its behavior breaks down like this:

- With stock semantics (Python 3.13 and prior), a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) is raised on the line defining `func`, since at that moment `Cls` is still an undefined name.

- With stringified annotations (when `from __future__ import annotations` is in effect), it prints `{'a': 'Cls', 'return': 'None'}`.

- With deferred evaluation (Python 3.14 onward), it prints `{'a': <class 'Cls'>, 'return': None}`.

Stock semantics were adopted at the point function annotations first appeared in Python 3.0 (through [**PEP 3107**](https://peps.python.org/pep-3107/)), since that was the most direct and obvious route to implementing annotations. That very same execution model carried over when variable annotations arrived in Python 3.6 (through [**PEP 526**](https://peps.python.org/pep-0526/)). Yet stock semantics created difficulties once annotations were employed as type hints — for example, the requirement to mention names not yet defined at the spot where the annotation appears. On top of that, evaluating annotations during module import incurred performance costs. As a result, Python 3.7 saw [**PEP 563**](https://peps.python.org/pep-0563/) add the option of keeping annotations as strings by way of the `from __future__ import annotations` syntax. The intention back then was to turn this into the default eventually, but a snag emerged: annotations stored as strings are harder to handle for anyone inspecting annotations at runtime. A competing proposal, [**PEP 649**](https://peps.python.org/pep-0649/), brought in the third execution model — deferred evaluation — which landed in Python 3.14. When `from __future__ import annotations` appears, stringified annotations continue to apply, though that behavior is slated for eventual removal.

[Subject index](INDEX.md) · [Previous](annotationlib-functionality-for-introspecting-annotations.md) · [Continue](annotationlib-format-class.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)

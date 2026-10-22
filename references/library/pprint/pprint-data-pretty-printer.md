# pprint — `pprint` — Data pretty printer

# Pprint

### `pprint` — Data pretty printer

**Source code:** [Lib/pprint.py](https://github.com/python/cpython/tree/3.14/Lib/pprint.py)

---

With the `pprint` module you can “pretty-print” any Python data structure into a shape that the interpreter can take back in as input. When the formatted structures hold objects that aren't basic Python types, the resulting representation may not load again. That happens, for instance, once files, sockets, or classes get involved, along with plenty of other objects that have no Python-literal form.

Wherever it can, the formatted representation holds an object on one line, splitting it across several lines only when it won't fit inside the permitted width — a width you can tune with the *width* parameter, which defaults to 80 characters.

Changed in version 3.9: Added support for pretty-printing [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace).

Changed in version 3.10: Added support for pretty-printing [`dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass).

[Subject index](INDEX.md) · [Continue](pprint-pp-to-pprint-isrecursive.md)

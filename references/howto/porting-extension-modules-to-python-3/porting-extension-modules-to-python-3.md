# Porting Extension Modules to Python 3

## Porting Extension Modules to Python 3

### Porting Extension Modules to Python 3

For moving extension modules over to Python 3, these references are the ones we suggest:

- Within *Supporting Python 3: An in-depth guide* — a volume devoted broadly to the shift away from Python 2 toward Python 3 — the [Migrating C extensions](http://python3porting.com/cextensions.html) chapter walks you step by step through converting an extension module.

- Coming out of the *py3c* project, the [Porting guide](https://py3c.readthedocs.io/en/latest/guide.html) lays out firmly held recommendations alongside accompanying code.

- [Recommended third party tools](https://docs.python.org/3.14/c-api/intro.html#c-api-tools) wrap Python’s C API behind higher-level abstractions. Adopting any of these usually demands that an extension be rebuilt against it, after which the library smooths over the gaps separating differing Python versions and implementations.

[Subject index](INDEX.md) · [Previous source context](../argument-clinic-how-to/argument-clinic-how-to.md)

# What's New In Python 3.9 / Type Hinting Generics in Standard Collections

### Type Hinting Generics in Standard Collections

Within type annotations the built-in container types ? `list`, `dict`, and friends ? may now serve directly as generics, sparing you the import of the capitalized counterparts (such as `List` or `Dict`) out of `typing`. A handful of additional standard-library types also became generic; `queue.Queue` is one example.

Example:

```python
def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)

```

Consult [**PEP 585**](https://peps.python.org/pep-0585/) for further detail. (Contributed by Guido van Rossum, Ethan Smith, and Batuhan Taşkaya in [bpo-39481](https://bugs.python.org/issue?@action=redirect&bpo=39481).)

[Subject index](INDEX.md) · [Previous source section](new-string-methods-to-remove-prefixes-and-suffixes.md) · [Next source section](new-parser.md) · [Release/subject declaration](summary-release-highlights.md)

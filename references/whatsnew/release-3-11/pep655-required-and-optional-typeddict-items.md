# What's New In Python 3.11 / PEP 655: Marking individual `TypedDict` items as required or not-required — typing

> (Contributed by Matthew Rahtz in [bpo-43224](https://bugs.python.org/issue?@action=redirect&bpo=43224), with contributions by Serhiy Storchaka and Jelle Zijlstra. PEP written by Mark Mendoza, Matthew Rahtz, Pradeep Kumar Srinivasan, and Vincent Siles.)

### PEP 655: Marking individual `TypedDict` items as required or not-required

[`Required`](https://docs.python.org/3.14/library/typing.html#typing.Required) and [`NotRequired`](https://docs.python.org/3.14/library/typing.html#typing.NotRequired) give you a clean mechanism for declaring whether particular keys within a [`TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) have to appear. Up to now you could only express that through inheritance.

By default every key remains mandatory, except when the *total* parameter is flipped to `False`, where instead every key defaults to not-required. The snippet below, for instance, defines a `TypedDict` carrying one mandatory key plus one optional one:

```python
class Movie(TypedDict):
   title: str
   year: NotRequired[int]

m1: Movie = {"title": "Black Panther", "year": 2018}  # OK
m2: Movie = {"title": "Star Wars"}  # OK (year is not required)
m3: Movie = {"year": 2022}  # ERROR (missing required field title)

```

This alternative spelling is equivalent:

```python
class Movie(TypedDict, total=False):
   title: Required[str]
   year: int

```

Consult [**PEP 655**](https://peps.python.org/pep-0655/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](pep-646-variadic-generics.md) · [Next source section](pep-673-self-type.md) · [Release/subject declaration](summary-release-highlights.md)

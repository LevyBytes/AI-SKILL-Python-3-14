# What's New In Python 3.11 / PEP 675: Arbitrary literal string type - typing

> (Contributed by James Hilton-Balfe in [bpo-46534](https://bugs.python.org/issue?@action=redirect&bpo=46534). PEP written by Pradeep Kumar Srinivasan and James Hilton-Balfe.)

### PEP 675: Arbitrary literal string type

The new [`LiteralString`](https://docs.python.org/3.14/library/typing.html#typing.LiteralString) annotation lets you signal that a function argument may hold any literal string type. With it a function can take arbitrary literal string types plus strings assembled from other literal strings. Type checkers are then positioned to require that risk-prone functions, like ones running SQL statements or shell commands, receive only static input, which guards against injection attacks.

To illustrate, a SQL query helper might carry this annotation:

```python
def run_query(sql: LiteralString) -> ...
    ...

def caller(
    arbitrary_string: str,
    query_string: LiteralString,
    table_name: LiteralString,
) -> None:
    run_query("SELECT * FROM students")       # ok
    run_query(query_string)                   # ok
    run_query("SELECT * FROM " + table_name)  # ok
    run_query(arbitrary_string)               # type checker error
    run_query(                                # type checker error
        f"SELECT * FROM students WHERE name = {arbitrary_string}"
    )

```

Consult [**PEP 675**](https://peps.python.org/pep-0675/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](pep-673-self-type.md) · [Next source section](pep-681-data-class-transforms.md) · [Release/subject declaration](summary-release-highlights.md)

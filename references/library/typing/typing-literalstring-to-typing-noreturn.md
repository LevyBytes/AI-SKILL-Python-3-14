# typing: `typing.LiteralString`, `typing.Never`, `typing.NoReturn`

typing.LiteralString

Special type that includes only literal strings.

Every string literal qualifies as a `LiteralString`, and so does any other `LiteralString`. By contrast, a value typed merely as `str` does not. A string built up by joining objects of type `LiteralString` is likewise valid as a `LiteralString`.

Example:

```python
def run_query(sql: LiteralString) -> None:
    ...

def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
    run_query("SELECT * FROM students")  # OK
    run_query(literal_string)  # OK
    run_query("SELECT * FROM " + literal_string)  # OK
    run_query(arbitrary_string)  # type checker error
    run_query(  # type checker error
        f"SELECT * FROM students WHERE name = {arbitrary_string}"
    )

```

`LiteralString` comes in handy for sensitive APIs in which strings supplied arbitrarily by users could cause trouble. To illustrate, both of the cases above that trigger type checker errors might be open to an SQL injection attack.

See [**PEP 675**](https://peps.python.org/pep-0675/) for more details.

Added in version 3.11.

 typing.Never

 typing.NoReturn

`Never` and `NoReturn` stand for the [bottom type](https://en.wikipedia.org/wiki/Bottom_type), a type whose set of members is empty.

You can apply them to signal that a function never gives back a value, like [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit):

```python
from typing import Never  # or NoReturn

def stop() -> Never:
    raise RuntimeError('no way')

```

Or to declare a function that ought never be invoked, since it admits no valid arguments, like `assert_never()`:

```python
from typing import Never  # or NoReturn

def never_call_me(arg: Never) -> None:
    pass

def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # type checker error
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)  # OK, arg is of type Never (or NoReturn)

```

Within the type system `Never` and `NoReturn` carry identical meaning, and static type checkers handle the two interchangeably.

Added in version 3.6.2: Added `NoReturn`.

Added in version 3.11: Added `Never`.

[Subject index](INDEX.md) · [Previous](typing-any-to-typing-anystr.md) · [Continue](typing-self.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special types](typing-any-to-typing-anystr.md)

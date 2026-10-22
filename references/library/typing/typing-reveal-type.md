# typing: `typing.reveal_type()`

typing.reveal_type(*obj*, */*)

Request that a static type checker disclose the inferred type of an expression.

Encountering a call to this function, a static type checker produces a diagnostic stating the argument's inferred type. As an example:

```python
x: int = 1
reveal_type(x)  # Revealed type is "builtins.int"

```

That makes it handy whenever you want to inspect how your type checker is treating a specific bit of code.

At runtime the function writes the runtime type of its argument to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) and gives the argument back unchanged (so the call can sit inside an expression):

```python
x = reveal_type(1)  # prints "Runtime type is int"
print(x)  # prints "1"

```

Be aware that the runtime type can differ from the type the checker statically inferred, being either narrower or broader.

Even when the name has not been imported from `typing`, most type checkers accept `reveal_type()` wherever it appears. That said, pulling the name in from `typing` lets your program run free of runtime errors and signals your intent more plainly.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](typing-cast-to-typing-assert-never.md) · [Continue](functions-and-decorators-signature-and-initial-contract.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Functions and decorators](typing-cast-to-typing-assert-never.md)

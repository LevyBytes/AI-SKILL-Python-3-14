# Automatically begin and end filling

### Automatically begin and end filling

As of Python 3.14, the `fill()` [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) is available in place of `begin_fill()` and `end_fill()`, handling the start and finish of a fill for you automatically. Consider this example:

```python
with fill():
    for i in range(4):
        forward(100)
        right(90)

forward(200)

```

That snippet accomplishes the same thing as:

```python
begin_fill()
for i in range(4):
    forward(100)
    right(90)
end_fill()

forward(200)

```

[Subject index](INDEX.md) · [Previous](get-started-as-quickly-as-possible.md) · [Continue](use-the-turtle-module-namespace.md)

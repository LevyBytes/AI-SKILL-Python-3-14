# compound statements: Multiple context managers and equivalent nesting

```python
with A() as a, B() as b:
    SUITE

```

is, in meaning, the same as:

```python
with A() as a:
    with B() as b:
        SUITE

```

Multi-item context managers can additionally be spread over several lines whenever the items are enclosed in parentheses. As an example:

```python
with (
    A() as a,
    B() as b,
):
    SUITE

```

Changed in version 3.1: Support for multiple context expressions.

Changed in version 3.10: Grouping parentheses may be used to split the statement across several lines.

See also

[**PEP 343**](https://peps.python.org/pep-0343/) - The “with” statement

The specification, background, and examples for the Python `with` statement.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-with-statement-suite-to-raise.md) · [Contract or procedure setup](the-with-statement-suite-to-raise.md) · [Previous source section](the-with-statement-suite-to-raise.md) · [Following source section](the-match-statement.md)

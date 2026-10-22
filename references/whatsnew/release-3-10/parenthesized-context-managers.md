# What's New In Python 3.10 / Parenthesized context managers

### New Features

### Parenthesized context managers

Wrapping a group of context managers in surrounding parentheses to span them across several lines is now permitted. That lets you lay out a lengthy series of context managers across several lines, much as you could already do with import statements. As an illustration, every one of the snippets below is now valid:

```python
with (CtxManager() as example):
    ...

with (
    CtxManager1(),
    CtxManager2()
):
    ...

with (CtxManager1() as example,
      CtxManager2()):
    ...

with (CtxManager1(),
      CtxManager2() as example):
    ...

with (
    CtxManager1() as example1,
    CtxManager2() as example2
):
    ...

```

You may additionally add a trailing comma after the final entry of the parenthesized group:

```python
with (
    CtxManager1() as example1,
    CtxManager2() as example2,
    CtxManager3() as example3,
):
    ...

```

The fresh parser makes this syntax possible by drawing on its non LL(1) capabilities. See [**PEP 617**](https://peps.python.org/pep-0617/) for further information.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](better-error-messages-syntaxerrors-syntaxerrors.md) · [Release/subject declaration](summary-release-highlights.md)

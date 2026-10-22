# 8.11. Annotations

### 8.11. Annotations

Changed in version 3.14: By default, annotations are now evaluated lazily.

Both variables and function parameters may bear [annotations](https://docs.python.org/3.14/glossary.html#term-annotation), formed by placing a colon after the name and then an expression:

```python
x: annotation = 1
def f(param: annotation): ...

```

A function may likewise bear a return annotation set off by an arrow:

```python
def f() -> annotation: ...

```

By convention annotations carry [type hints](https://docs.python.org/3.14/glossary.html#term-type-hint), though the language does not require this, and generally an annotation can hold arbitrary expressions. Annotations being present does not alter the code’s runtime semantics, unless some mechanism that introspects and consumes the annotations is in play (such as [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) or [`functools.singledispatch()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatch)).

Out of the box, evaluation of annotations is deferred within an [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). Put differently, running the code that surrounds an annotation does not trigger that annotation's evaluation. Rather, the interpreter stashes away enough detail to evaluate it down the line whenever something asks for it. For carrying out that evaluation, the [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib) module supplies the necessary tooling.

Whenever the [future statement](https://docs.python.org/3.14/reference/simple_stmts.html#future) `from __future__ import annotations` appears, every annotation is kept instead in string form:

```python
>>> from __future__ import annotations
>>> def f(param: annotation): ...
>>> f.__annotations__
{'param': 'annotation'}

```

A later Python release is slated to deprecate this future statement and drop it altogether, though that will not happen until after Python 3.13 has hit its end of life (refer to [**PEP 749**](https://peps.python.org/pep-0749/)). Where it is in effect, introspection helpers such as [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) and [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) stand a reduced chance of resolving annotations while the program runs.

Footnotes

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](generic-type-aliases.md)

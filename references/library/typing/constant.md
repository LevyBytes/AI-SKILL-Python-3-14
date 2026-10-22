# typing: TYPE_CHECKING imports and deferred annotation inspection

When a module is costly to import and holds nothing but types meant for annotations, you can place its import safely within an `if TYPE_CHECKING:` block. Doing so keeps the module from being loaded at runtime; because annotations aren’t evaluated eagerly (see [**PEP 649**](https://peps.python.org/pep-0649/)), referencing symbols that aren’t defined inside annotations causes no trouble—provided you never inspect them afterward. During static type analysis your tool flips `TYPE_CHECKING` to `True`, so the module does get imported and its types are checked correctly at that stage.

Usage:

```python
if TYPE_CHECKING:
    import expensive_mod

def fun(arg: expensive_mod.SomeType) -> None:
    local_var: expensive_mod.AnotherType = other_fun()

```

When you do, on occasion, have to inspect annotations at runtime that might reference undefined symbols, reach for [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations), passing a `format` of either [`annotationlib.Format.STRING`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.STRING) or [`annotationlib.Format.FORWARDREF`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.FORWARDREF), which lets you fetch the annotations safely and avoids a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError).

Added in version 3.5.2.

[Subject index](INDEX.md) · [Continue](deprecated-aliases.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Constant](typing-type-checking.md) · [Owning module, declaration or section: typing.TYPE_CHECKING](typing-type-checking.md) · [Preceding source contract and version conditions](typing-type-checking.md)

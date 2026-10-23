# annotationlib - Limitations of the `FORWARDREF` format

### Limitations of the `FORWARDREF` format

The `FORWARDREF` format strives to yield genuine values wherever it can, swapping in `ForwardRef` objects for whatever resists resolution. Roughly the same Limitations that dog the `STRING` format apply here too: annotations that act on literals or that invoke unsupported expression types can throw exceptions once evaluated through the `FORWARDREF` format.

A handful of examples showing how unsupported expressions behave appear below:

```pycon
>>> from annotationlib import get_annotations, Format
>>> def zerodiv(x: 1 / 0): ...
>>> get_annotations(zerodiv, format=Format.STRING)
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
>>> get_annotations(zerodiv, format=Format.FORWARDREF)
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
>>> def ifexp(x: 1 if y else 0): ...
>>> get_annotations(ifexp, format=Format.STRING)
{'x': '1'}

```

[Subject index](INDEX.md) · [Previous](ast-starred-to-ast-yieldfrom.md) · [Continue](security-implications-of-introspecting-annotations.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)

# inspect: `inspect.get_annotations()`

inspect.get_annotations(*obj*, ***, *globals=None*, *locals=None*, *eval_str=False*, *format=annotationlib.Format.VALUE*)

Work out the annotations dict for an object.

This stands as an alias for [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations); consult that function's documentation for fuller details.

Caution

This function might run arbitrary code embedded in annotations. Consult [Security implications of introspecting annotations](https://docs.python.org/3.14/library/annotationlib.html#annotationlib-security) for further details.

Added in version 3.10.

Changed in version 3.14: This function now serves as an alias for [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations). Invoking it as `inspect.get_annotations` keeps working.

[Subject index](INDEX.md) · [Previous](inspect-getclasstree-to-inspect-unwrap.md) · [Continue](inspect-frameinfo-class.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Classes and functions](inspect-getclasstree-to-inspect-unwrap.md)

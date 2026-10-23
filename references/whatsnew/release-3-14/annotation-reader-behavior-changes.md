# What's new in Python 3.14 / Changes in annotations (**PEP 649** and **PEP 749**) / Implications for readers of `__annotations__` - annotationlib, dataclasses

#### Implications for readers of `__annotations__`

Code that pulls the [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attribute off objects might need adjustment so it cooperates with callers that depend on deferred annotation evaluation. One option, mirroring what [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) now does, is to invoke [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) under the [`FORWARDREF`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format.FORWARDREF) format.

Partial backports of a portion of the [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib) module's functionality, including the [`Format`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format) enum and the [`get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) function, come from the external [typing_extensions](https://pypi.org/project/typing_extensions/) package. With them you can author cross-version code that exploits the new Python 3.14 behavior.

#### Related changes

[Subject index](INDEX.md) · [Previous source section](changes-in-annotations-implications-for-annotated-code.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](changes-in-annotations.md) · [Following release/subject continuation](changes-in-annotations-related-changes.md)

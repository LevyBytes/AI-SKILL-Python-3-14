# annotationlib — `annotationlib` — Functionality for introspecting annotations

### `annotationlib` — Functionality for introspecting annotations

Added in version 3.14.

**Source code:** [Lib/annotationlib.py](https://github.com/python/cpython/tree/3.14/Lib/annotationlib.py)

---

Use the `annotationlib` module when you need utilities for inspecting [annotations](https://docs.python.org/3.14/glossary.html#term-annotation) attached to modules, classes, and functions.

Because annotations are [lazily evaluated](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation), they frequently hold forward references pointing at objects that have not been defined yet at the moment the annotation comes into being. To handle this, the module supplies a collection of low-level utilities that fetch annotations dependably, including the tricky scenarios where forward references and other corner cases come into play.

Annotations can be retrieved through this module in three principal formats (refer to `Format`), with each suited to a distinct kind of use case:

- `VALUE` evaluates the annotations and hands back their value. While this is the simplest format to deal with, it can raise errors — for instance, when an annotation points at a name that is undefined.

- `FORWARDREF` hands back `ForwardRef` objects for any annotation that cannot be resolved, which lets you examine the annotations without forcing their evaluation. Reach for this when the annotations you are handling might carry unresolved forward references.

- `STRING` gives back the annotations rendered as a string, much like the form they take in the source file. Documentation generators that aim to present annotations in an easy-to-read manner find this useful.

To retrieve annotations, the principal entry point is the `get_annotations()` function. Hand it a function, class, or module, and it yields an annotations dictionary in whichever format you asked for. Beyond that, the module exposes ways to operate directly on the [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function) responsible for evaluating annotations — namely `get_annotate_from_class_namespace()` and `call_annotate_function()` — plus the `call_evaluate_function()` function for handling [evaluate functions](https://docs.python.org/3.14/glossary.html#term-evaluate-function).

Caution

Nearly everything in this module is capable of running arbitrary code; consult the security section for further details.

See also

[**PEP 649**](https://peps.python.org/pep-0649/) put forward the model that governs how annotations currently behave in Python.

[**PEP 749**](https://peps.python.org/pep-0749/) built on several facets of [**PEP 649**](https://peps.python.org/pep-0649/) and brought in the `annotationlib` module.

[Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html#annotations-howto) lays out recommended practices for handling annotations.

[typing-extensions](https://pypi.org/project/typing-extensions/) ships a backport of `get_annotations()` usable on older Python releases.

[Subject index](INDEX.md) · [Continue](annotation-semantics.md)

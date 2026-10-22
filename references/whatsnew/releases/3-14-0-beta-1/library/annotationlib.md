# Python 3.14.0 beta 1 / library / annotationlib

[gh-119180](https://github.com/python/cpython/issues/119180): Let [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) return successfully under the `FORWARDREF` format whenever evaluating the annotations throws something other than [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) or [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

[gh-125618](https://github.com/python/cpython/issues/125618): Introduce a *format* parameter for [`annotationlib.ForwardRef.evaluate()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef.evaluate). Resolving annotations under the `FORWARDREF` format now works in additional situations that formerly would have thrown an exception.

[gh-132805](https://github.com/python/cpython/issues/132805): Correct the faulty processing of nested non-constant values within the FORWARDREF format in [`annotationlib`](https://docs.python.org/3.14/library/annotationlib.html#module-annotationlib).

[gh-132064](https://github.com/python/cpython/issues/132064): [`annotationlib.get_annotations()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotations) now relies on the `__annotate__` attribute when it exists, even where `__annotations__` is missing. On top of that, the function now throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) if handed an object carrying no annotatins.

[gh-132491](https://github.com/python/cpython/issues/132491): Give `annotationlib.value_to_string` the new name [`annotationlib.type_repr()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.type_repr) and improve how it deals with function objects.

[gh-132426](https://github.com/python/cpython/issues/132426): Introduce [`annotationlib.get_annotate_from_class_namespace()`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.get_annotate_from_class_namespace) to assist with reaching annotations from within metaclasses, and drop `annotationlib.get_annotate_function`.

[gh-129463](https://github.com/python/cpython/issues/129463): Comparing [`annotationlib.ForwardRef`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.ForwardRef) objects no longer relies on the internal `__code__` and `__ast_node__` attributes, which serve as caches.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

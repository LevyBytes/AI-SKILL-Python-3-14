# Python 3.14.0 alpha 1 / library / functions and types

[gh-119506](https://github.com/python/cpython/issues/119506): Stop the `io.TextIOWrapper.write()` method from corrupting its internal buffer when the method is invoked again while that buffer is being flushed.

[gh-123341](https://github.com/python/cpython/issues/123341): Gives `tkinter.Event` a [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) so that type subscripting works at runtime. Adonis Rakateli wrote the patch.

[gh-119180](https://github.com/python/cpython/issues/119180): Sort out how classes carrying custom metaclasses are treated in `annotationlib.get_annotations`.

[gh-122129](https://github.com/python/cpython/issues/122129): Better the treatment of method descriptors and wrappers within the help title.

[gh-82951](https://github.com/python/cpython/issues/82951): Pickling objects whose `__qualname__` is complex (think unbound methods and nested classes) by name will no longer pull parent objects into value-serialization under pickle protocols < 4.

[gh-122081](https://github.com/python/cpython/issues/122081): Stop a crash inside the `decimal.IEEEContext()` optional function, which is reachable through the `EXTRA_FUNCTIONALITY` configuration flag.

[gh-81936](https://github.com/python/cpython/issues/81936): The `help()` and `showtopic()` methods now honor a configured *output* argument given to `pydoc.Helper`, skipping the pager in those situations. Enrico Tröger authored the patch.

[gh-120485](https://github.com/python/cpython/issues/120485): Supply an override for `allow_reuse_port` on classes that subclass `socketserver.TCPServer` wherever `allow_reuse_address` already gets overridden.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

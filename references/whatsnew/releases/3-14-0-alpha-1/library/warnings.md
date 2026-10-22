# Python 3.14.0 alpha 1 / library / warnings

[gh-121163](https://github.com/python/cpython/issues/121163): Accept `all` as a legitimate `action` value for [`warnings.simplefilter()`](https://docs.python.org/3.14/library/warnings.html#warnings.simplefilter) and [`warnings.filterwarnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.filterwarnings).

[gh-122088](https://github.com/python/cpython/issues/122088): [`@warnings.deprecated`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated) now carries over the coroutine status from functions and methods, ensuring [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction) gives the right answer.

[gh-119562](https://github.com/python/cpython/issues/119562): Delete `ast.Num`, `ast.Str`, `ast.Bytes`, `ast.NameConstant` and `ast.Ellipsis`, every one of which had been emitting deprecation warnings ever since Python 3.12. Alex Waygood authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

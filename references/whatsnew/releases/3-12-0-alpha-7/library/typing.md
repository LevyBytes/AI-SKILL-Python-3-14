# Python 3.12.0 alpha 7 / library / typing

[gh-88965](https://github.com/python/cpython/issues/88965): typing: Resolve a bug around substitution within custom classes generic over a [`ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec). Earlier, once the `ParamSpec` had been substituted with a parameters list that itself held a [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), there was no way to substitute that `TypeVar` afterward. The fix lands here.

Nikita Sobolev wrote the patch.

[gh-102615](https://github.com/python/cpython/issues/102615): Typing: The `repr` for generic aliases of classes parameterized over a [`ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) reads better now. (A parameter list is shown using square brackets.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

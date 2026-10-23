# What's New In Python 3.3 / PEP 362: Function Signature Object - functools, inspect

### PEP 362: Function Signature Object

Introspecting python callables becomes simple and direct with a new [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) function. It accommodates a wide assortment of callables: python functions whether or not they are decorated, classes, and [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) objects. The new [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature), [`inspect.Parameter`](https://docs.python.org/3.14/library/inspect.html#inspect.Parameter) and [`inspect.BoundArguments`](https://docs.python.org/3.14/library/inspect.html#inspect.BoundArguments) classes record details about the call signatures ? among them annotations, default values, the kinds of parameters, and bound arguments ? which greatly eases the job of writing decorators along with any code that checks or adjusts calling signatures or arguments.

See also

[**PEP 362**](https://peps.python.org/pep-0362/): - Function Signature Object

Authored as a PEP by Brett Cannon, Yury Selivanov, Larry Hastings, Jiwon Seo; built by Yury Selivanov.

[Subject index](INDEX.md) · [Previous source section](pep-412-key-sharing-dictionary.md) · [Next source section](pep-421-adding-sys-implementation.md) · [Release/subject declaration](summary-release-highlights.md)

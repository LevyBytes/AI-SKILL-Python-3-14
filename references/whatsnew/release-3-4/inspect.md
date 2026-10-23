# What's New In Python 3.4 / inspect - enum, functools, inspect

### inspect

The [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module provides a simple [command line interface](https://docs.python.org/3.14/library/inspect.html#inspect-module-cli) for rapidly viewing source text and related details about modules, classes and functions. (Contributed by Claudiu Popa and Nick Coghlan in [bpo-18626](https://bugs.python.org/issue?@action=redirect&bpo=18626).)

[`unwrap()`](https://docs.python.org/3.14/library/inspect.html#inspect.unwrap) lets you peel apart the chains of wrapper functions produced by [`functools.wraps()`](https://docs.python.org/3.14/library/functools.html#functools.wraps) (along with any other API that stamps a `__wrapped__` attribute onto a wrapper). (Contributed by Daniel Urban, Aaron Iles and Nick Coghlan in [bpo-13266](https://bugs.python.org/issue?@action=redirect&bpo=13266).)

While building the new [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module, the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module picked up markedly stronger handling of custom `__dir__` methods and of dynamic class attributes delivered via metaclasses. (Contributed by Ethan Furman in [bpo-18929](https://bugs.python.org/issue?@action=redirect&bpo=18929) and [bpo-19030](https://bugs.python.org/issue?@action=redirect&bpo=19030).)

[`getfullargspec()`](https://docs.python.org/3.14/library/inspect.html#inspect.getfullargspec) and `getargspec()` are now built atop the [`signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) API. That lets them cope with a far wider set of callables, among them ones carrying `__signature__` attributes, ones whose metadata comes from argument clinic, [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) objects and others. Be aware that, in contrast with `signature()`, these helpers continue to disregard `__wrapped__` attributes and report the already bound first argument for bound methods, so switching your code over to `signature()` directly remains necessary when those capabilities matter. (Contributed by Yury Selivanov in [bpo-17481](https://bugs.python.org/issue?@action=redirect&bpo=17481).)

[`signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) handles duck types of CPython functions, which brings along support for functions built with Cython. (Contributed by Stefan Behnel and Yury Selivanov in [bpo-17159](https://bugs.python.org/issue?@action=redirect&bpo=17159).)

[Subject index](INDEX.md) · [Previous source section](importlib.md) · [Next source section](ipaddress.md) · [Release/subject declaration](release-highlights.md)

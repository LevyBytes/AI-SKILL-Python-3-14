# Python 3.14.1 final / core and builtins / threads and concurrency

[gh-140257](https://github.com/python/cpython/issues/140257): Resolve a data race spanning interpreter_clear() and take_gil() over eval_breaker while finalization runs with daemon threads.

[gh-128640](https://github.com/python/cpython/issues/128640): Resolve a crash that occurs while threads are used inside a subinterpreter.

[gh-139653](https://github.com/python/cpython/issues/139653): Raise a `RecursionError`, or fire a fatal error, solely when the stack pointer sits both beneath the limit pointer *and* over the stack base. Whenever it lands outside those bounds, treat the situation as acceptable. Doing so blocks false positives that surface when user-space threads exchange stacks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

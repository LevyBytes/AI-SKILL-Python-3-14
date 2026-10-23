# What's New In Python 3.6 / inspect - inspect

### inspect

For comprehension and generator expression scopes, the compiler emits implicit `.0` parameters; the [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) function now surfaces those as though they were positional-only parameters named `implicit0`. (Contributed by Jelle Zijlstra in [bpo-19611](https://bugs.python.org/issue?@action=redirect&bpo=19611).)

So that migrating from Python 2.7 and the old `inspect.getargspec()` API causes less code churn, the formerly documented plan to deprecate [`inspect.getfullargspec()`](https://docs.python.org/3.14/library/inspect.html#inspect.getfullargspec) has been undone. That function helps with single-source Python 2/3 codebases, yet for brand-new code the fuller [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) interface stays the advised choice. (Contributed by Nick Coghlan in [bpo-27172](https://bugs.python.org/issue?@action=redirect&bpo=27172))

[Subject index](INDEX.md) · [Previous source section](importlib.md) · [Next source section](json.md) · [Release/subject declaration](summary-release-highlights.md)

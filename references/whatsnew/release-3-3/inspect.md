# What's New In Python 3.3 / inspect - inspect

### inspect

There is a new [`getclosurevars()`](https://docs.python.org/3.14/library/inspect.html#inspect.getclosurevars) function. It tells you how every name the function body touches is currently bound and where each name resolved, which simplifies checking the internal state while testing code built on stateful closures.

Meador Inge and Nick Coghlan landed this ([bpo-13062](https://bugs.python.org/issue?@action=redirect&bpo=13062)).

There is also a new [`getgeneratorlocals()`](https://docs.python.org/3.14/library/inspect.html#inspect.getgeneratorlocals) function. It tells you how the local variables in the generator’s stack frame are currently bound, which simplifies checking the internal state while testing generators.

Meador Inge landed this ([bpo-15153](https://bugs.python.org/issue?@action=redirect&bpo=15153)).

[Subject index](INDEX.md) · [Previous source section](imaplib.md) · [Next source section](io.md) · [Release/subject declaration](summary-release-highlights.md)

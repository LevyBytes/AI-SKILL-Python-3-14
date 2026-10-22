# rlcompleter.Completer: `complete()`

complete(*text*, *state*)

Return the next possible completion for *text*.

When called by the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module, this method is invoked one time after another with `state == 0, 1, 2, ...` right up until the method yields `None`.

When invoked for *text* holding no period character (`'.'`), it completes against names presently defined in [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__), [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) and keywords (as the [`keyword`](https://docs.python.org/3.14/library/keyword.html#module-keyword) module defines them).

When invoked for a dotted name, it will attempt to evaluate whatever has no plain side-effects (functions go un-evaluated, though it can trigger calls to [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__)) as far as the final segment, then locate matches for the remainder by way of the [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) function. Whatever exception surfaces while the expression is evaluated gets caught, suppressed, and [`None`](https://docs.python.org/3.14/library/constants.html#None) is handed back.

[Subject index](INDEX.md) · [Previous](rlcompleter-completer-class.md) · [Owning module, declaration or section: rlcompleter](rlcompleter-completer-class.md) · [Owning module, declaration or section: rlcompleter.Completer](rlcompleter-completer-class.md)

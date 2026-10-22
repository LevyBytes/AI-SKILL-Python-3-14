# Python 2.5 changes: Generator close and finalization

Bringing in the `close()` method carries one side effect that isn't immediately apparent. Because `close()` is invoked when a generator gets garbage-collected, that means the generator's code gets one final opportunity to run before the generator is destroyed. That last opportunity means `try...finally` statements within generators can now be relied upon to work; the [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause is now always going to get its chance to run. So the syntactic restriction that barred you from mixing [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statements with a `try...finally` suite has been lifted. That might look like a small scrap of language trivia, yet pairing generators with `try...finally` is in fact required in order to build the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement laid out by [**PEP 343**](https://peps.python.org/pep-0343/). I’ll examine that new statement in the section that follows.

A further, even more obscure effect of this change: in the past, a generator's `gi_frame` attribute was invariably a frame object. Now it's possible for `gi_frame` to be `None` after the generator has run dry.

See also

[**PEP 342**](https://peps.python.org/pep-0342/) - Coroutines via Enhanced Generators

PEP authored by Guido van Rossum together with Phillip J. Eby; the implementation came from Phillip J. Eby. Contains examples showing some fancier ways to use generators as coroutines.

[Subject index](INDEX.md) · [Previous source section](pep-342-new-generator-features.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Release/subject declaration](pep-342-new-generator-features.md) · [Following release/subject continuation](generator-send-and-throw-protocols.md)

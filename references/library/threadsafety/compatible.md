# Compatible

### Compatible

Such a function or operation is fine to invoke across several threads *as long as* the caller adds suitable external synchronization, say by keeping a [lock](https://docs.python.org/3.14/glossary.html#term-lock) held throughout each call. Lacking that coordination, simultaneous calls might trigger [race conditions](https://docs.python.org/3.14/glossary.html#term-race-condition) or [data races](https://docs.python.org/3.14/glossary.html#term-data-race).

Example: a function that reads or writes an object whose inner state has no lock guarding it. The caller has to guarantee that two threads never touch one object simultaneously.

[Subject index](INDEX.md) · [Previous](incompatible.md) · [Continue](safe-on-distinct-objects.md)

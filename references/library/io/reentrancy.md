# io - Reentrancy

### Reentrancy

Reentrancy is not supported by binary buffered objects — that is, any instance of `BufferedReader`, `BufferedWriter`, `BufferedRandom` or `BufferedRWPair`. Such reentrant calls rarely occur under ordinary conditions, though performing I/O within a [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) handler is one way to trigger them. Should a thread attempt to step back into a buffered object it is in the middle of using, the result is a raised [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Keep in mind that this restriction still permits a separate thread to enter the same buffered object.

By the same token, the rule carries over to text files, because [`open()`](https://docs.python.org/3.14/library/functions.html#open) wraps a buffered object within a `TextIOWrapper`. Standard streams fall under this too, which is why the built-in [`print()`](https://docs.python.org/3.14/library/functions.html#print) is likewise impacted.

[Subject index](INDEX.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)

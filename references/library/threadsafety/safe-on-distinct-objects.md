# Safe on distinct objects

### Safe on distinct objects

Such a function or operation is fine to invoke across several threads with no external synchronization, so long as every thread works on a **different** object. Two threads are allowed to call the function at once, but they must never hand it the same object (or objects whose underlying state overlaps) as arguments.

Example: a function that updates struct fields through non-atomic writes. Two threads may each invoke the function on a struct instance of their own without issue, yet simultaneous calls on the *same* instance demand external synchronization.

[Subject index](INDEX.md) · [Previous](compatible.md) · [Continue](safe-on-shared-objects.md)

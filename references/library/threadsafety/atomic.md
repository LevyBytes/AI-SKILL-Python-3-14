# Atomic

### Atomic

Such a function or operation looks [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation) to other threads - from their vantage point it runs in an instant. This represents the most robust kind of thread safety.

Example: [`PyMutex_IsLocked()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_IsLocked) does an atomic read of the mutex state and is callable from whichever thread at whatever moment.

[Subject index](INDEX.md) · [Previous](safe-on-shared-objects.md) · [Continue](thread-safety-for-list-objects.md)

# contextlib — Reusable context managers

### Reusable context managers

Set apart from both the single use and the reentrant varieties are the “reusable” context managers (or, spelled out fully, “reusable, but not reentrant” ones, given that reentrant context managers count as reusable as well). They permit repeated use, yet break (or otherwise go wrong) when that particular instance is already active within an enclosing with statement.

[`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) serves as a reusable but non-reentrant context manager (should you want a reentrant lock, turn to [`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock) instead).

`ExitStack` is one more reusable but non-reentrant context manager, since on exit from any with statement it fires *every* callback registered at that moment, no matter where each callback was originally added:

```python
>>> from contextlib import ExitStack
>>> stack = ExitStack()
>>> with stack:
...     stack.callback(print, "Callback: from first context")
...     print("Leaving first context")
...
Leaving first context
Callback: from first context
>>> with stack:
...     stack.callback(print, "Callback: from second context")
...     print("Leaving second context")
...
Leaving second context
Callback: from second context
>>> with stack:
...     stack.callback(print, "Callback: from outer context")
...     with stack:
...         stack.callback(print, "Callback: from inner context")
...         print("Leaving inner context")
...     print("Leaving outer context")
...
Leaving inner context
Callback: from inner context
Callback: from outer context
Leaving outer context

```

The printed output makes it clear that putting one stack object through several with statements behaves fine, whereas nesting them empties the stack once the innermost with statement ends, which you will rarely actually want.

Reaching for distinct `ExitStack` instances rather than recycling one sidesteps that issue:

```python
>>> from contextlib import ExitStack
>>> with ExitStack() as outer_stack:
...     outer_stack.callback(print, "Callback: from outer context")
...     with ExitStack() as inner_stack:
...         inner_stack.callback(print, "Callback: from inner context")
...         print("Leaving inner context")
...     print("Leaving outer context")
...
Leaving inner context
Callback: from inner context
Leaving outer context
Callback: from outer context

```

[Subject index](INDEX.md) · [Previous](reentrant-context-managers.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)

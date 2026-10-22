# contextvars — `contextvars` — Context Variables

### `contextvars` — Context Variables

---

APIs for storing, reading, and administering context-local state come from this module. Declaring and operating on *Context Variables* is what the `ContextVar` class is for. To oversee the current context inside asynchronous frameworks, rely on the `copy_context()` function together with the `Context` class.

Stateful context managers ought to reach for Context Variables rather than [`threading.local()`](https://docs.python.org/3.14/library/threading.html#threading.local), which keeps their state from leaking unexpectedly into other code once they run under concurrency.

See also [**PEP 567**](https://peps.python.org/pep-0567/) for additional details.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](context-variables.md) · [Continue](contextvars-contextvar-class.md)

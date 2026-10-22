# object.__init__(*self*[, *...*])

object.__init__(*self*[, *...*])

Invoked once the instance exists (having been built by `__new__()`), yet before it reaches the caller. The arguments match those passed to the class constructor expression. Where a base class provides an `__init__()` method, the derived class’s `__init__()` method, if it has one, is obliged to call it explicitly so the base class portion of the instance is initialized properly; for instance: `super().__init__([args...])`.

Since `__new__()` and `__init__()` cooperate while building objects (`__new__()` makes it, and `__init__()` tailors it), `__init__()` is not permitted to return any non-`None` value; if it does, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised at runtime.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Previous source section](object-new.md) · [Following source section](object-del.md)

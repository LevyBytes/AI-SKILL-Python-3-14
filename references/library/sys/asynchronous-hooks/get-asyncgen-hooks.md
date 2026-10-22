# sys.get_asyncgen_hooks

sys.get_asyncgen_hooks()

Hands back an *asyncgen_hooks* object, much like a [`namedtuple`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) shaped as `(firstiter, finalizer)`, in which *firstiter* and *finalizer* are meant to be either `None` or functions that accept an [asynchronous generator iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator-iterator) as their argument and serve to schedule the finalization of an asynchronous generator through an event loop.

Added in version 3.6: See [**PEP 525**](https://peps.python.org/pep-0525/) for more details.

Note

This function is provided provisionally for now (refer to [**PEP 411**](https://peps.python.org/pep-0411/) for the details.)

[API family](INDEX.md) · [sys context index](../INDEX.md).

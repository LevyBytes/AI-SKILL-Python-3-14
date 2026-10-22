# frame.clear()

frame.clear()

This method wipes out every reference to [local variables](https://docs.python.org/3.14/reference/executionmodel.html#naming) that the frame holds. Additionally, when the frame was part of a [generator](https://docs.python.org/3.14/glossary.html#term-generator), that generator gets finalized. Doing so assists in tearing apart reference cycles that involve frame objects (for instance, while catching an [exception](https://docs.python.org/3.14/library/exceptions.html#bltin-exceptions) and retaining its traceback to use afterward).

[`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised if the frame is currently executing or suspended.

Added in version 3.4.

Changed in version 3.13: Trying to clear a frame that is suspended now raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) (just as has always held true for frames that are executing).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Owning language section](frame-objects.md) · [Owning language section](frame-object-methods.md) · [Previous source section](frame-object-methods.md) · [Following source section](traceback-objects.md)

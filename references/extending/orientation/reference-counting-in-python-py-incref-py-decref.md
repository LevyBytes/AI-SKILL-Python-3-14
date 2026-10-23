# Reference Counting in Python - Py_INCREF, Py_DECREF

### 1.10.1. Reference Counting in Python

Two macros exist, `Py_INCREF(x)` and `Py_DECREF(x)`, which manage the incrementing and decrementing of the reference count. [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) additionally frees the object when the count drops to zero. To stay flexible, it avoids calling `free()` directly — instead it makes a call through a function pointer held in the object's *type object*. To that end (among others), every object likewise carries a pointer to its type object.

So the big question stands: when should `Py_INCREF(x)` and `Py_DECREF(x)` be used? First let's lay out some terminology. No one "owns" an object; you can, however, *own a reference* to one. An object's reference count is then defined as the tally of owned references pointing at it. Whoever owns a reference bears the duty of calling [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) once that reference is no longer wanted. A reference's ownership may be handed off. Three ways exist to dispose of an owned reference: hand it on, store it, or call `Py_DECREF()`. Neglecting to dispose of an owned reference produces a memory leak.

You can also *borrow* [2] a reference to an object. Whoever borrows a reference should not call [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF). The borrower must not cling to the object beyond the lifetime of the owner it borrowed from. Using a borrowed reference once the owner has disposed of it courts using freed memory and ought to be steered clear of entirely [3].

Borrowing's edge over owning a reference is that you needn't bother disposing of the reference along every conceivable path through the code — put differently, a borrowed reference carries no risk of leaking when an early exit is taken. Borrowing's drawback against owning is that certain subtle scenarios exist where, within code that looks correct, a borrowed reference may end up used after the owner it was borrowed from has in fact already disposed of it.

Calling [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) turns a borrowed reference into an owned one. This leaves the status of the owner the reference came from untouched — it forges a new owned reference and confers full owner responsibilities (the new owner must dispose of the reference properly, just as the original owner must).

[Subject index](INDEX.md) · [Previous source section](reference-counts.md) · [Next source section](ownership-rules-and-pydict-setitem.md)

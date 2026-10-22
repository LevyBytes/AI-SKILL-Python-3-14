# introduction C API: Reference ownership and transfer principles

#### Reference Count Details

The clearest way to make sense of how Python/C API functions behave with reference counts is through *ownership of references*. Ownership applies to references, not ever to objects (objects go unowned: they stay shared throughout). "Owning a reference" amounts to taking responsibility for invoking Py_DECREF on it whenever the reference stops being needed. Ownership is transferable too, which means the code taking over ownership of the reference then bears responsibility for eventually letting it go via [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) or [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) once it's no longer needed — or for handing that responsibility along (typically to its own caller). Where a function hands ownership of a reference along to its caller, we say the caller takes in a *new* reference. Where no ownership changes hands, we say the caller *borrows* the reference. A [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) calls for nothing to be done.

On the flip side, whenever a calling function hands in a reference to an object, two outcomes are possible: either the function *steals* a reference to the object, or it doesn't. *Stealing a reference* means that, as you hand a reference along to a function, that function takes it that ownership is now its own, and you no longer carry any responsibility for it.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](reference-counts.md) · [Continued contract in following source](reference-count-details-int.md)

# Limited API Caveats

### Limited API Caveats

Bear in mind that building with `Py_LIMITED_API` is *not* a full assurance that code abides by the Limited API or the Stable ABI. `Py_LIMITED_API` reaches only definitions, yet an API also brings other concerns, expected semantics among them.

One thing `Py_LIMITED_API` won't catch is invoking a function with arguments invalid in an older Python version. Picture a function that begins to accept `NULL` for an argument. Under Python 3.9, `NULL` now triggers a default behavior, but under Python 3.8 the argument is used as given, producing a `NULL` dereference and a crash. The same reasoning applies to fields of structs.

A further wrinkle is that a handful of struct fields stay visible at present when `Py_LIMITED_API` is defined, despite belonging to the Limited API.

Given all this, we advise testing an extension against *all* the minor Python versions it claims to support, and ideally building with the *lowest* one.

We further advise reading through the documentation of every API you call to confirm it is explicitly named part of the Limited API. Even when `Py_LIMITED_API` is defined, a small number of private declarations leak through for technical reasons (or even by accident, as bugs).

Keep in mind too that the Limited API need not be stable: building with `Py_LIMITED_API` under Python 3.8 means the extension will run on Python 3.12, but it won't necessarily *compile* on Python 3.12. Notably, portions of the Limited API may be deprecated and removed, so long as the Stable ABI remains stable.

[Subject index](INDEX.md) · [Previous source contract](limited-api-scope-and-performance.md) · [Following source contract](platform-considerations.md)

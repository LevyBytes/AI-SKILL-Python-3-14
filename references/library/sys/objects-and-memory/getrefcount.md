# sys.getrefcount

sys.getrefcount(*object*)

Report the reference count of the *object*. What comes back is usually one greater than you would guess, since it counts the (temporary) reference handed in as an argument to `getrefcount()`.

Keep in mind that the figure returned might not truly mirror how many references to the object are really held. As one case, certain objects are [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) and carry an extremely high refcount that bears no relation to the genuine reference count. For that reason, treat anything beyond 0 or 1 as unreliable.

**CPython implementation detail:** You can recognize [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) objects carrying a large reference count through `_is_immortal()`.

Changed in version 3.12: Immortal objects now carry enormous refcounts that bear no relation to the genuine count of references aimed at the object.

[API family](INDEX.md) · [sys context index](../INDEX.md).

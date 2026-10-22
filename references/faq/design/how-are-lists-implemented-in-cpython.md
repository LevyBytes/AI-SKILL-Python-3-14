# How are lists implemented in CPython?

### How are lists implemented in CPython?

CPython's lists are in fact variable-length arrays, not linked lists in the Lisp style. The implementation employs a contiguous array of references to other objects, and it holds a pointer to that array along with the array's length within a list head structure.

This renders indexing a list `a[i]` an operation whose cost stays independent of the list's size or the index's value.

As items get appended or inserted, the array of references is resized. A bit of cleverness goes into boosting the performance of repeated appends; when the array has to grow, some surplus space is set aside so the next several operations avoid an actual resize.

[Subject index](INDEX.md)

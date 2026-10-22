# ssizeargfunc PySequenceMethods.sq_inplace_repeat

ssizeargfunc PySequenceMethods.sq_inplace_repeat

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_sq_inplace_repeat` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*
Sharing a signature with [`PySequence_InPlaceRepeat()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_InPlaceRepeat), this function backs it. The expectation is that it mutate its first operand and hand it back. Leaving this slot as `NULL` is allowed; then `PySequence_InPlaceRepeat()` defers to [`PySequence_Repeat()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Repeat). The augmented assignment `*=` also reaches for it, once it has tried numeric in-place multiplication through the `nb_inplace_multiply` slot.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pysequencemethods-to-pysequencemethods-sq-inplace-concat.md) · [Previous source contract](pybufferprocs.md)

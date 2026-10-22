# unicode C API: `PyUnicode_RichCompare()`, `PyUnicode_Format()`, `PyUnicode_Contains()`, `PyUnicode_InternInPlace()`, `PyUnicode_InternFromString()`, `PyUnicode_CHECK_INTERNED()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_RichCompare([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *left, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *right, int op)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Rich compare two Unicode strings and return one of the following:

- `NULL` in case an exception was raised

- [`Py_True`](https://docs.python.org/3.14/c-api/bool.html#c.Py_True) or [`Py_False`](https://docs.python.org/3.14/c-api/bool.html#c.Py_False) for successful comparisons

- [`Py_NotImplemented`](https://docs.python.org/3.14/c-api/object.html#c.Py_NotImplemented) in case the type combination is unknown

Possible values for *op* are [`Py_GT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_GT), [`Py_GE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_GE), [`Py_EQ`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_EQ), [`Py_NE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_NE), [`Py_LT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_LT), and [`Py_LE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_LE).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Format([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *format, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produce a fresh string object out of *format* together with *args*; the effect parallels `format % args`.

 int PyUnicode_Contains([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *substr)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Determine if *unicode* holds *substr* somewhere inside it, giving back true or false to suit.

The *substr* value must reduce to a single-element Unicode string. Any error makes the call yield `-1`.

 void PyUnicode_InternInPlace([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **p_unicode)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Intern, right where it sits, the argument *p_unicode. You have to supply the address of a pointer variable that itself refers to a Python Unicode string object. Where an already-interned string matches *p_unicode, the call points *p_unicode at that one — dropping the reference to the former string object and forging a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) onto the interned object; failing such a match, it leaves *p_unicode untouched and interns it.

(To clear things up: for all the reference chatter here, treat this call as reference-neutral. Ownership of whatever you hand in is on you; once the call returns, that incoming reference is no longer yours, yet the result now is.)

No exception is ever raised by this call. When something fails, it returns its argument as-is and skips interning.

A subclass instance of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) cannot be interned — put another way, PyUnicode_CheckExact(*p_unicode) is required to hold true. Where it does not, the argument stays as it was, exactly as happens with any other error.

Keep in mind that an interned string is not “immortal”. Holding onto a reference to the result is what lets you reap interning's benefit.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_InternFromString(const char *str)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Pairs `PyUnicode_FromString()` with `PyUnicode_InternInPlace()` in one call, intended for strings allocated statically.

Give back a fresh (“owned”) reference, pointing either at a newly interned Unicode string object or at a previously interned object that shares the same value.

Python might retain a reference to the result, or render it [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) so that prompt garbage collection no longer reaches it. When you mean to intern a boundless stream of distinct strings — those arriving from user input, for instance — it's wiser to invoke `PyUnicode_FromString()` and `PyUnicode_InternInPlace()` yourself.

 unsigned int PyUnicode_CHECK_INTERNED([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *str)

Give back something non-zero when *str* has been interned, or zero when it hasn't. A string is required for the *str* argument, but that goes unverified. This call cannot fail.

**CPython implementation detail:** Beyond signaling interning, a non-zero result can encode extra detail about *how* the string got interned. Both what those non-zero values denote and the intern-related specifics of any given string are liable to shift from one CPython version to the next.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-concat-to-pyunicode-tailmatch.md) · [Previous source contract](pyunicode-count-to-pyunicode-comparewithasciistring.md) · [Following source contract](pyunicodewriter.md)

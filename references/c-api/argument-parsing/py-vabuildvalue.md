# argument parsing C API: `Py_VaBuildValue()`

`k` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned long]

Turns a C unsigned long into a Python integer object.

`L` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [long long]

Turns a C long long into a Python integer object.

`K` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned long long]

Turns a C unsigned long long into a Python integer object.

`n` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [[`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Turns a C [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) into a Python integer.

`p` ([`bool`](https://docs.python.org/3.14/library/functions.html#bool)) [int]

Turns a C int into a Python [`bool`](https://docs.python.org/3.14/library/functions.html#bool) object.

Note that this format calls for an `int` argument. In contrast to most other settings in C, variadic arguments here aren't automatically coerced into a fitting type. To obtain a fitting `int` value from some other type — a pointer or a float, say — use `(x) ? 1 : 0` or `!!x`.

Added in version 3.14.

`c` ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) of length 1) [char]

Turns a C int that stands for a byte into a length-1 Python [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

`C` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) of length 1) [int]

Turns a C int that stands for a character into a length-1 Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object.

`d` ([`float`](https://docs.python.org/3.14/library/functions.html#float)) [double]

Turns a C double into a Python floating-point number.

`f` ([`float`](https://docs.python.org/3.14/library/functions.html#float)) [float]

Turns a C float into a Python floating-point number.

`D` ([`complex`](https://docs.python.org/3.14/library/functions.html#complex)) [Py_complex *]

Turns a C [`Py_complex`](https://docs.python.org/3.14/c-api/complex.html#c.Py_complex) structure into a Python complex number.

`O` (object) [PyObject *]

Forwards a Python object as-is while forging a new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to it (that is, bumping its reference count up by one). Should the incoming object be a `NULL` pointer, the assumption is that the call which produced the argument hit an error and set an exception. Hence `Py_BuildValue()` returns `NULL` yet raises no exception of its own. When no exception has been raised so far, [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) gets set.

`S` (object) [PyObject *]

Same as `O`.

`N` (object) [PyObject *]

Matches `O`, but forges no new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference). It helps when an object constructor invoked within the argument list is what produced the object.

`O&` (object) [*converter*, *anything*]

Turns *anything* into a Python object by way of a *converter* function. That function receives *anything* (which ought to be compatible with void*) as its argument and is expected to give back a “new” Python object, or `NULL` should an error arise.

`(items)` ([`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)) [*matching-items*]

Turns a run of C values into a Python tuple holding just as many items.

`[items]` ([`list`](https://docs.python.org/3.14/library/stdtypes.html#list)) [*matching-items*]

Turns a run of C values into a Python list holding just as many items.

`{items}` ([`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)) [*matching-items*]

Turns a run of C values into a Python dictionary. Every consecutive pair of C values contributes a single dictionary item, acting as the key and the value in turn.

Where the format string holds an error, the [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) exception gets set and `NULL` is returned.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_VaBuildValue(const char *format, va_list vargs)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The same as `Py_BuildValue()`, aside from taking a va_list in place of a variadic argument list.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-buildvalue.md)

# Py_ssize_t PyLong_AsNativeBytes(PyObject *pylong, void *buffer, Py_ssize_t n_bytes, int flags)

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyLong_AsNativeBytes([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong, void *buffer, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) n_bytes, int flags)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Writes the Python integer value *pylong* into a native *buffer* whose size is *n_bytes*. Set *flags* to `-1` for behavior close to a C cast, or to the values listed below to steer the behavior.

On error `-1` is returned with an exception raised. That can occur when *pylong* cannot be read as an integer, or when *pylong* was negative while the `Py_ASNATIVEBYTES_REJECT_NEGATIVE` flag was active.

In every other case, the count of bytes needed to hold the value is returned. When that count is at or below *n_bytes*, the whole value made it across. The full *n_bytes* of the buffer are populated, with any leftover bytes filled by repetitions of the sign bit.

Whenever the returned count exceeds *n_bytes*, truncation happened: only as many of the value's lowest bits as fit get written, while the upper bits drop away. That mirrors how a C-style downcast normally behaves.

Note

An overflow does not count as an error here. Whenever the count handed back tops *n_bytes*, the highest-order bits were thrown away.

`0` will never be returned.

Values are always copied as two's-complement.

Usage example:

```c
int32_t value;
Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, &value, sizeof(value), -1);
if (bytes < 0) {
    // Failed. A Python exception was set with the reason.
    return NULL;
}
else if (bytes <= (Py_ssize_t)sizeof(value)) {
    // Success!
}
else {
    // Overflow occurred, but 'value' contains the truncated
    // lowest bits of pylong.
}

```

Handing a *n_bytes* of zero gives back the size a buffer would need to be in order to hold the whole value. The figure can run a little above the strict minimum, though never wildly so. When *n_bytes=0*, *buffer* is allowed to be `NULL`.

Note

Handing *n_bytes=0* to this routine does not reliably reveal how many bits the value occupies.

When the Python value has an unknown size and you want all of it, invoke the function twice: once to learn the required buffer size, then again to populate it:

```c
// Ask how much space we need.
Py_ssize_t expected = PyLong_AsNativeBytes(pylong, NULL, 0, -1);
if (expected < 0) {
    // Failed. A Python exception was set with the reason.
    return NULL;
}
assert(expected != 0);  // Impossible per the API definition.
uint8_t *bignum = malloc(expected);
if (!bignum) {
    PyErr_SetString(PyExc_MemoryError, "bignum malloc failed.");
    return NULL;
}
// Safely get the entire value.
Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, bignum, expected, -1);
if (bytes < 0) {  // Exception has been set.
    free(bignum);
    return NULL;
}
else if (bytes > expected) {  // This should not be possible.
    PyErr_SetString(PyExc_RuntimeError,
        "Unexpected bignum truncation after a size check.");
    free(bignum);
    return NULL;
}
// The expected success given the above pre-check.
// ... use bignum ...
free(bignum);

```

You give *flags* either as `-1` (`Py_ASNATIVEBYTES_DEFAULTS`), which chooses defaults closest to a C cast, or as a mix of the remaining flags from the table that follows. Be aware that `-1` may not be mixed with any other flag.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Continued contract in following source](pylong-aspid-to-pylong-getinfo.md) · [Previous source contract](pylong-asdouble-to-pylong-asvoidptr.md)

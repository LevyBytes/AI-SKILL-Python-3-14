# Pack functions

### Pack functions

Beginning at *p*, the pack routines lay down 2, 4 or 8 bytes. The int argument *le* is non-zero when you want the bytes string little-endian (exponent last, at `p+1`, `p+3`, or `p+6` and `p+7`), and zero when you want big-endian (exponent first, at *p*). To go with the native endian, lean on the `PY_BIG_ENDIAN` constant: it holds `1` on a big endian processor and `0` on a little endian one.

Return value: `0` when everything is fine, `-1` when an error occurs (with an exception set, most often [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError)).

A pair of difficulties arise on non-IEEE platforms:

- Its behavior is left undefined whenever *x* is a NaN or an infinity.

- `-0.0` and `+0.0` yield one and the same bytes string.

 int PyFloat_Pack2(double x, char *p, int le)

Encode a C double into the IEEE 754 binary16 half-precision format.

 int PyFloat_Pack4(double x, char *p, int le)

Encode a C double into the IEEE 754 binary32 single precision format.

 int PyFloat_Pack8(double x, char *p, int le)

Encode a C double into the IEEE 754 binary64 double precision format.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyfloatobject-to-py-nan.md) · [Previous source contract](pack-and-unpack-functions.md) · [Following source contract](pyfloat-unpack2-to-pyfloat-unpack8.md)

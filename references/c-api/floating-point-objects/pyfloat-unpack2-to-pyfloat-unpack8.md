# Unpack functions

### Unpack functions

Beginning at *p*, the unpack routines take in 2, 4 or 8 bytes. The int argument *le* is non-zero when the bytes string is little-endian (exponent last, at `p+1`, `p+3` or `p+6` and `p+7`), and zero when it is big-endian (exponent first, at *p*). To go with the native endian, lean on the `PY_BIG_ENDIAN` constant: it holds `1` on a big endian processor and `0` on a little endian one.

Return value: the double that was unpacked. Where an error occurs this is `-1.0` and [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) holds true (with an exception set, most often [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError)).

Note that on a non-IEEE platform it declines to unpack any bytes string standing for a NaN or an infinity.

 double PyFloat_Unpack2(const char *p, int le)

Decode the IEEE 754 binary16 half-precision format into a C double.

 double PyFloat_Unpack4(const char *p, int le)

Decode the IEEE 754 binary32 single precision format into a C double.

 double PyFloat_Unpack8(const char *p, int le)

Decode the IEEE 754 binary64 double precision format into a C double.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyfloatobject-to-py-nan.md) · [Previous source contract](pyfloat-pack2-to-pyfloat-pack8.md) · [Following source contract](../frame-objects/pyframeobject-to-pyframe-getgenerator.md)

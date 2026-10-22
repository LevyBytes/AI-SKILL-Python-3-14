# Bit-packing macros

### Bit-packing macros

 uint32_t Py_PACK_FULL_VERSION(int major, int minor, int micro, int release_level, int release_serial)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Hands back the supplied version packed into one 32-bit integer laid out as shown below:

| Argument | No. of bits | Bit mask | Bit shift | Example values |  |
| --- | --- | --- | --- | --- | --- |
| `3.4.1a2` | `3.10.0` |  |  |  |  |
| *major* | 8 | `0xFF000000` | 24 | `0x03` | `0x03` |
| *minor* | 8 | `0x00FF0000` | 16 | `0x04` | `0x0A` |
| *micro* | 8 | `0x0000FF00` | 8 | `0x01` | `0x00` |
| *release_level* | 4 | `0x000000F0` | 4 | `0xA` | `0xF` |
| *release_serial* | 4 | `0x0000000F` | 0 | `0x2` | `0x0` |

For example:

| Version | `Py_PACK_FULL_VERSION` arguments | Encoded version |
| --- | --- | --- |
| `3.4.1a2` | `(3, 4, 1, 0xA, 2)` | `0x030401a2` |
| `3.10.0` | `(3, 10, 0, 0xF, 0)` | `0x030a00f0` |

Any bits in the arguments that fall outside the valid range are dropped. Put differently, the macro may be defined like this:

```c
#ifndef Py_PACK_FULL_VERSION
#define Py_PACK_FULL_VERSION(X, Y, Z, LEVEL, SERIAL) ( \
   (((X) & 0xff) << 24) |                              \
   (((Y) & 0xff) << 16) |                              \
   (((Z) & 0xff) << 8) |                               \
   (((LEVEL) & 0xf) << 4) |                            \
   (((SERIAL) & 0xf) << 0))
#endif

```

Chiefly `Py_PACK_FULL_VERSION` is a macro meant for `#if` directives, though it can additionally be reached as an exported function.

Added in version 3.14.

 uint32_t Py_PACK_VERSION(int major, int minor)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Stands in for `Py_PACK_FULL_VERSION(major, minor, 0, 0, 0)`. Although the value it yields matches no actual Python release, it still serves well for numeric comparisons.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](build-time-version-constants.md) · [Previous source contract](py-version.md)

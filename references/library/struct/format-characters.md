# struct — Format Characters

### Format Characters

Here is what each format character signifies; how a C value maps to a Python value ought to be clear from their respective types. That ‘Standard size’ column gives the packed value’s byte count under standard size — in other words, whenever the format string opens with one of `'<'`, `'>'`, `'!'` or `'='`. Under native size, the packed value’s size instead varies by platform.

| Format | C Type | Python type | Standard size | Notes |
| --- | --- | --- | --- | --- |
| `x` | pad byte | no value |  | (7) |
| `c` | char | bytes of length 1 | 1 |  |
| `b` | signed char | int | 1 | (2) |
| `B` | unsigned char | int | 1 | (2) |
| `?` | _Bool | bool | 1 | (1) |
| `h` | short | int | 2 | (2) |
| `H` | unsigned short | int | 2 | (2) |
| `i` | int | int | 4 | (2) |
| `I` | unsigned int | int | 4 | (2) |
| `l` | long | int | 4 | (2) |
| `L` | unsigned long | int | 4 | (2) |
| `q` | long long | int | 8 | (2) |
| `Q` | unsigned long long | int | 8 | (2) |
| `n` | `ssize_t` | int |  | (2), (3) |
| `N` | `size_t` | int |  | (2), (3) |
| `e` | _Float16 | float | 2 | (4), (6) |
| `f` | float | float | 4 | (4) |
| `d` | double | float | 8 | (4) |
| `F` | float complex | complex | 8 | (10) |
| `D` | double complex | complex | 16 | (10) |
| `s` | char[] | bytes |  | (9) |
| `p` | char[] | bytes |  | (8) |
| `P` | void* | int |  | (2), (5) |

Changed in version 3.3: Added support for the `'n'` and `'N'` formats.

Changed in version 3.6: Added support for the `'e'` format.

Changed in version 3.14: Added support for the `'F'` and `'D'` formats.

See also

The [`array`](https://docs.python.org/3.14/library/array.html#module-array) and [ctypes](https://docs.python.org/3.14/library/ctypes.html#ctypes-fundamental-data-types) modules, plus outside packages such as [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__), rely on comparable type codes that nonetheless differ a little.

Notes:

1.

Conversion code `'?'` lines up with the _Bool type that the C standards have specified ever since C99. Under standard mode a single byte stands for it.

2.

Suppose you try to pack a non-integer through one of the integer conversion codes: if that value carries a [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method, the code invokes it to turn the argument into an integer ahead of packing.

Changed in version 3.2: non-integers now have the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method consulted.

3.

You can reach the `'n'` and `'N'` conversion codes solely under native size, which you get by default or via the `'@'` byte order character. Where standard size is concerned, just pick whichever of the remaining integer formats suits your application.

4.

With conversion codes `'f'`, `'d'` and `'e'`, whatever the platform’s own floating-point format happens to be, the packed bytes always follow the IEEE 754 binary32, binary64 or binary16 format — matching `'f'`, `'d'` or `'e'` in turn.

5.

The `'P'` format character is reachable only under native byte ordering, which you obtain by default or through the `'@'` byte order character. When the `'='` byte order character is given, it settles on little- or big-endian according to the host machine. Because the struct module declines to treat that as native ordering, `'P'` cannot be used there.

6.

The 2008 revision of the [IEEE 754 standard](https://en.wikipedia.org/wiki/IEEE_754-2008_revision) brought in the IEEE 754 binary16 “half precision” type. It carries a sign bit, a 5-bit exponent, and 11-bit precision (of which 10 bits are actually stored), and across its full-precision range it spans roughly `6.1e-05` up to `6.5e+04`. Few C compilers support it: you reach it as the _Float16 type when the compiler implements Annex H of the C23 standard. On a usual machine an unsigned short serves to hold it, though not to compute with it. For further detail consult the Wikipedia article on the [half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format).

7.

During packing, a single NUL byte is emitted by `'x'`.

8.

What the `'p'` format character encodes is a “Pascal string” — that is, a brief variable-length string kept inside a *fixed number of bytes*, set by the count. Stored first is one byte giving either the string’s length or 255, whichever turns out smaller, and after it come the string’s own bytes. Should the byte string handed to `pack()` overrun the count minus 1, only its first `count-1` bytes get kept. Should it fall short of `count-1`, null bytes pad it out so that count bytes exactly are consumed in total. Keep in mind that with `unpack()`, the `'p'` format character eats `count` bytes, yet the `bytes` object you get back is capped at 255 bytes. While packing, you may supply arguments of type [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

9.

With the `'s'` format character the count stands for how long the byte string is, rather than the repeat count it means for the other format characters; thus `'10s'` denotes one 10-byte string going to or from a single Python byte string, while `'10c'` denotes 10 individual one-byte character elements (say `cccccccccc`) going to or from ten distinct Python byte objects. (Examples shows the contrast in practice.) Omit the count and it falls back to 1. On packing, the byte string is trimmed or null-padded as needed so it fits. On unpacking, the `bytes` object you receive holds precisely the stated byte count. In the special case `'0s'`, you get one empty byte string, whereas `'0c'` yields 0 characters. While packing, arguments of type [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) are allowed.

10.

With the `'F'` and `'D'` format characters, no matter the platform’s native floating-point format, each piece of the complex number is packed using the IEEE 754 binary32 and binary64 format. Observe that the complex types `F` and `D` are present without any condition, even though C treats complex types as an optional feature. Per the C11 standard, every complex type maps to a two-element C array whose entries are, in order, the real and the imaginary part.

You may put an integer repeat count ahead of a format character. By way of illustration, the format string `'4h'` is precisely equivalent to `'hhhh'`.

Any whitespace sitting between formats is skipped; even so, a count and the format it belongs to must stay free of whitespace.

Pack a value `x` through one of the integer formats — `'b'`, `'B'`, `'h'`, `'H'`, `'i'`, `'I'`, `'l'`, `'L'`, `'q'`, `'Q'` — and if `x` lies beyond the range that format permits, `struct.error` gets raised.

Changed in version 3.1: in earlier releases a handful of the integer formats wrapped values that fell out of range, emitting [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) rather than `struct.error`.

With the `'?'` format character, what comes back is one of [`True`](https://docs.python.org/3.14/library/constants.html#True) or [`False`](https://docs.python.org/3.14/library/constants.html#False). On packing, the code looks at the argument object’s truth value. The native or standard bool form of 0 or 1 is what gets packed, and on unpacking anything non-zero reads back as `True`.

[Subject index](INDEX.md) · [Previous](byte-order-size-and-alignment.md) · [Continue](examples.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)

# Encodings

### Encodings

To recap the prior section: a Unicode string is a series of code points, integers ranging from 0 up to `0x10FFFF` (1,114,111 decimal). That series of code points must be held in memory as a collection of **code units**, and those **code units** are subsequently mapped onto 8-bit bytes. We call the rules that convert a Unicode string into a byte sequence a **character encoding**, or simply an **encoding**.

One obvious first idea is to adopt 32-bit integers as the code unit and rely on the CPU’s native handling of 32-bit integers. Under such a scheme, the string “Python” could be laid out like this:

```none
   P           y           t           h           o           n
0x50 00 00 00 79 00 00 00 74 00 00 00 68 00 00 00 6f 00 00 00 6e 00 00 00
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23

```

Although this representation is simple, putting it to use brings several drawbacks.

1.

It lacks portability; processors differ in how they order bytes.

2.

It squanders a great deal of space. Across most texts, the bulk of the code points fall below 127, or below 255, so plenty of room ends up filled with `0x00` bytes. That string above consumes 24 bytes versus the 6 bytes an ASCII representation requires. The extra RAM use isn’t a big deal (desktop machines carry gigabytes of RAM, and strings rarely grow that big), yet quadrupling our consumption of disk and network bandwidth cannot be tolerated.

3.

It doesn’t mesh with existing C functions like `strlen()`, which means a fresh family of wide string functions would be required.

For these reasons the encoding sees little use, and people opt instead for other encodings that are more efficient and convenient, UTF-8 among them.

UTF-8 ranks among the most widely used encodings, and Python frequently treats it as the default. The letters UTF stand for “Unicode Transformation Format”, while the ‘8’ signals that 8-bit values feature in the encoding. (UTF-16 and UTF-32 encodings exist too, though they appear less often than UTF-8.) The rules UTF-8 follows are these:

1.

When the code point is < 128, the matching byte value represents it.

2.

When the code point is >= 128, it expands into a series of two, three, or four bytes, with every byte in that series sitting between 128 and 255.

UTF-8 offers a number of handy properties:

1.

Any Unicode code point can be handled by it.

2.

A Unicode string becomes a byte sequence whose embedded zero bytes appear only where they stand for the null character (U+0000). As a result, C functions like `strcpy()` can process UTF-8 strings, and they can travel through protocols that treat zero bytes as nothing other than end-of-string markers.

3.

ASCII text also qualifies as valid UTF-8 text.

4.

UTF-8 stays reasonably compact; one or two bytes suffice for the majority of commonly used characters.

5.

When bytes are lost or corrupted, you can still locate the beginning of the next UTF-8-encoded code point and resynchronize. On top of that, random 8-bit data is unlikely to resemble valid UTF-8.

6.

UTF-8 is a byte oriented encoding. Under the encoding, every character maps to a definite sequence of one or more bytes. That sidesteps the byte-ordering problems that crop up with integer and word oriented encodings, such as UTF-16 and UTF-32, where the byte sequence shifts according to the hardware that encoded the string.

[Subject index](INDEX.md) · [Previous source context](definitions.md) · [Following source context](references.md)

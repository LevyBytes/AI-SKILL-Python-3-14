# Pack and Unpack functions

### Pack and Unpack functions

An efficient, platform-neutral means of keeping floating-point values as byte strings is what the pack and unpack functions deliver. From a C double the Pack routines yield a bytes string, while from such a bytes string the Unpack routines yield a C double. How many bytes sit in the bytes string is set by the suffix (2, 4 or 8).

Wherever a platform looks to be using IEEE 754 formats, these functions operate by copying bits. Elsewhere, the 2-byte format matches the IEEE 754 binary16 half-precision format, the 4-byte (32-bit) format matches the IEEE 754 binary32 single precision format, and the 8-byte format matches the IEEE 754 binary64 double precision format — though INFs and NaNs (where the platform has such things) are not packed correctly, and trying to unpack a bytes string that holds an IEEE INF or NaN throws an exception.

Note that the NaN type might go unpreserved on IEEE platforms (signaling NaNs turn into quiet NaNs) — on x86 systems running in 32-bit mode, for one.

Where a non-IEEE platform offers more precision, or a wider dynamic range, than IEEE 754 covers, certain values cannot be packed; where one offers less precision, or a narrower dynamic range, certain values cannot be unpacked. The outcome under such conditions is partly a matter of chance (regrettably).

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyfloatobject-to-py-nan.md) · [Previous source contract](py-huge-val-to-py-is-nan.md) · [Following source contract](pyfloat-pack2-to-pyfloat-pack8.md)

# sys.hash_info

sys.hash_info

A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) that exposes parameters of the numeric hash implementation. For fuller detail on how numeric types are hashed, see [Hashing of numeric types](https://docs.python.org/3.14/library/stdtypes.html#numeric-hash).

hash_info.width

The width in bits used for hash values

 hash_info.modulus

The prime modulus P used for numeric hash scheme

 hash_info.inf

The hash value returned for a positive infinity

 hash_info.nan

(This attribute is no longer used)

 hash_info.imag

The multiplier used for the imaginary part of a complex number

 hash_info.algorithm

The name of the algorithm for hashing of str, bytes, and memoryview

 hash_info.hash_bits

The internal output size of the hash algorithm

 hash_info.seed_bits

The size of the seed key of the hash algorithm

 hash_info.cutoff

Cutoff for small string DJBX33A optimization in range `[1, cutoff)`.

Added in version 3.2.

Changed in version 3.4: Added *algorithm*, *hash_bits*, *seed_bits*, and *cutoff*.

[API family](INDEX.md) · [sys context index](../INDEX.md).

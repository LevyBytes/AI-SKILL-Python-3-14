# hashing C API: `Py_uhash_t`, `Py_HASH_ALGORITHM`, `Py_HASH_FNV`, `Py_HASH_SIPHASH24`, `Py_HASH_SIPHASH13`, `Py_HASH_CUTOFF`, `PyHASH_MODULUS`, `PyHASH_BITS`, `PyHASH_MULTIPLIER`, `PyHASH_INF`, `PyHASH_IMAG`

type Py_uhash_t

An unsigned integer; this is the type that holds a hash value.

Added in version 3.2.

 Py_HASH_ALGORITHM

A number that names which hashing algorithm applies to [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview).

You can read that algorithm's name off [`sys.hash_info.algorithm`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.algorithm).

Added in version 3.4.

 Py_HASH_FNV

 Py_HASH_SIPHASH24

 Py_HASH_SIPHASH13

Numbers you match against `Py_HASH_ALGORITHM` to find out which hashing algorithm is in effect. Selecting that algorithm is done through configure's [`--with-hash-algorithm`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-hash-algorithm) option.

Added in version 3.4: Add `Py_HASH_FNV` and `Py_HASH_SIPHASH24`.

Added in version 3.11: Add `Py_HASH_SIPHASH13`.

 Py_HASH_CUTOFF

When a buffer's length falls inside `[1, Py_HASH_CUTOFF)`, DJBX33A handles its hashing rather than whatever `Py_HASH_ALGORITHM` points to.

- Setting `Py_HASH_CUTOFF` to 0 turns the optimization off.

- The value of `Py_HASH_CUTOFF` has to be zero or above and no greater than 7.

Because colliding strings come together more readily there, a 32-bit build wants a smaller cutoff than a 64-bit one. Picking 7 where the platform is 64-bit and 5 where it is 32-bit leaves a reasonable safety margin.

It maps onto the [`sys.hash_info.cutoff`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.cutoff) constant.

Added in version 3.4.

 PyHASH_MODULUS

The numeric hash scheme relies on the [Mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime) `P = 2**n -1`.

It maps onto the [`sys.hash_info.modulus`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.modulus) constant.

Added in version 3.13.

 PyHASH_BITS

Within `PyHASH_MODULUS`, this is the `n` to which `P` is raised.

Added in version 3.13.

 PyHASH_MULTIPLIER

The prime that multiplies strings along with several other hashes.

Added in version 3.13.

 PyHASH_INF

Whatever hash value comes back for a positive infinity.

It maps onto the [`sys.hash_info.inf`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.inf) constant.

Added in version 3.13.

 PyHASH_IMAG

Whatever multiplier applies to a complex number's imaginary component.

It maps onto the [`sys.hash_info.imag`](https://docs.python.org/3.14/library/sys.html#sys.hash_info.imag) constant.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyhash-api.md) · [Previous source contract](py-hash-t.md) · [Following source contract](pyhash-funcdef-to-pyobject-generichash.md)

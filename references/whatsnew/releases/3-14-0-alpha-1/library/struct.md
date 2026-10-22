# Python 3.14.0 alpha 1 / library / struct

[gh-124248](https://github.com/python/cpython/issues/124248): Eliminated a possible crash where [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) processed zero-width "Pascal string" fields (`0p`).

[gh-121249](https://github.com/python/cpython/issues/121249): Where the compiler offers C11 complex arithmetic, the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module now backs the float complex and double complex C types. Patch by Sergey B Kirpichev.

[gh-125118](https://github.com/python/cpython/issues/125118): Within the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module, refrain from copying arbitrary values into _Bool.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

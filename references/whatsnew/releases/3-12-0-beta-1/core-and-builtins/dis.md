# Python 3.12.0 beta 1 / core and builtins / dis

[gh-87729](https://github.com/python/cpython/issues/87729): Introduce [`LOAD_SUPER_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_SUPER_ATTR) (plus a specialization for `super().method()`) to accelerate `super().method()` and `super().attr`. This renders `super().method()` about 2.3x faster, putting it within 20% of an ordinary method call's speed. Vladimir Matveev and Carl Meyer wrote the patch.

[gh-88691](https://github.com/python/cpython/issues/88691): Lower the count of inline [`CACHE`](https://docs.python.org/3.14/library/dis.html#opcode-CACHE) entries used by [`CALL`](https://docs.python.org/3.14/library/dis.html#opcode-CALL).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

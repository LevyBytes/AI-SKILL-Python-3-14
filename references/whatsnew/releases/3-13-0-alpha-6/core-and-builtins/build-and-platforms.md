# Python 3.13.0 alpha 6 / core and builtins / build and platforms

[gh-117494](https://github.com/python/cpython/issues/117494): Pulled the instruction sequence data structure out of compile.c and into instruction_sequence.c.

[gh-108362](https://github.com/python/cpython/issues/108362): Build an incremental cyclic garbage collector. Gathering the old generation piece by piece removes the need to scan the whole heap at once. For programs holding large heaps this can shrink the worst-case pause time dramatically.

Cut the generation count from three down to two. Two spaces, ?visited? and ?pending?, now divide the old generation.

Collection proceeds across two steps:: * The young generation plus a slice of the pending space form an increment. * That increment is examined and its survivors land at the tail of the visited space.

Once the collecting space runs empty, the pair of spaces trade places.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

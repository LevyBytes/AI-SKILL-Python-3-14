# Python 3.14.0 alpha 1 / core and builtins / memory and lifetimes

[gh-125174](https://github.com/python/cpython/issues/125174): Reference-count handling for immortal objects is made sturdier. An immortal object still counts as immortal even when its reference count strays from the original by as much as a billion (or half a billion on 32 bit builds).

[gh-123083](https://github.com/python/cpython/issues/123083): Close a possible use-after-free inside `STORE_ATTR_WITH_HINT`.

[gh-122697](https://github.com/python/cpython/issues/122697): Plug memory leaks at interpreter shutdown under the free-threaded build, and also the reporting of leaked memory blocks through [`-X showrefcount`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X).

[gh-122417](https://github.com/python/cpython/issues/122417): Under the free-threaded build, heap type objects now keep part of their reference counts spread across per-thread arrays. Doing so cuts contention on a heap type's reference count fields while instances of that same type are being created or destroyed across several threads at once.

[gh-120298](https://github.com/python/cpython/issues/120298): Close a use-after free inside `list_richcompare_impl` reachable through some carefully crafted evil input.

[gh-119726](https://github.com/python/cpython/issues/119726): Boost both the speed and the memory use of C function calls made from JIT code on AArch64. Diego Russo authored this.

[gh-116017](https://github.com/python/cpython/issues/116017): Streamline the warmup machinery behind "side exits" in JIT code, which buys marginally better performance together with marginally lower memory usage on most platforms.

[gh-116017](https://github.com/python/cpython/issues/116017): Lower JIT memory use by reclaiming, at intervals, the storage held by code that runs rarely. Long-running programs are the most likely beneficiaries of a smaller memory footprint here.

[gh-121368](https://github.com/python/cpython/issues/121368): Close a race condition in `_PyType_Lookup` under the free-threaded build that stemmed from a missing memory fence. The gap could cause `_PyType_Lookup` to hand back wrong results on arm64.

[gh-124547](https://github.com/python/cpython/issues/124547): While deallocating an object that has inline values and whose `__dict__` is still alive, the dictionary is now cleared if allocating memory for the inline values fails. This averts an interpreter crash.

[gh-119726](https://github.com/python/cpython/issues/119726): For calls to C functions, the JIT now emits tighter code, yielding up to 0.8% memory savings and a 1.5% speed gain on AArch64. Diego Russo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

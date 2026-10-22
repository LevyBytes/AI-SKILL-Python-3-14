# Python 3.14.0 alpha 1 / core and builtins / collections and iteration

[gh-122208](https://github.com/python/cpython/issues/122208): A dictionary watcher now fires the PyDict_EVENT_ADDED event only once the insertion sits in a known-good state to succeed.

[gh-125039](https://github.com/python/cpython/issues/125039): In the cases generator, `this_instr` and `prev_instr` are now made const.

[gh-93691](https://github.com/python/cpython/issues/93691): Correct the source locations on the instructions generated for the iterator of a for statement.

[gh-121860](https://github.com/python/cpython/issues/121860): Stop a crash while rematerializing a managed dictionary after its deletion.

[gh-121795](https://github.com/python/cpython/issues/121795): Speed up set membership testing, along with `set.remove()` and `set.discard()`, whenever the argument happens to be a set.

[gh-121497](https://github.com/python/cpython/issues/121497): Repair a defect that stopped the REPL from honoring history correctly while an input hook was set. Pablo Galindo authored this.

[gh-121012](https://github.com/python/cpython/issues/121012): Tier 2 execution now keeps list iterators exhausted from the moment they reach exhaustion.

[gh-119011](https://github.com/python/cpython/issues/119011): Make `type.__type_params__` hand back an empty tuple rather than a descriptor.

[gh-124642](https://github.com/python/cpython/issues/124642): A scalability problem in free-threaded builds, affecting lock-free dictionary reads in multi-threaded scenarios, is resolved

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

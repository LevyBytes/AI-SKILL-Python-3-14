# collections: `collections.deque`

### `deque` objects

 *class *collections.deque([*iterable*[, *maxlen*]])

Hands back a fresh deque object filled left-to-right (by way of `append()`) using the data from *iterable*. When *iterable* is left out, the new deque starts out empty.

Deques generalize stacks and queues (you say the name like "deck," a shortened form of "double-ended queue"). They allow thread-safe, memory-efficient appends and pops on either end, with roughly equal *O*(1) performance whichever direction you go.

While [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) objects offer comparable operations, they are tuned for quick fixed-length operations and bear *O*(*n*) memory-movement costs on `pop(0)` and `insert(0, v)` operations, which shift both the size and the position of the underlying data representation.

When *maxlen* is left out or set to `None`, deques may stretch to any length. Otherwise, the deque is capped at the stated maximum length. After a length-bounded deque reaches capacity, adding new items discards a matching count of items off the far end. Length-bounded deques deliver behavior akin to the `tail` filter in Unix. They also help when tracking transactions and similar pools of data where only the latest activity matters.

Deques are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the type of their contents.

Deque objects support the following methods:

[Subject index](INDEX.md) · [Previous](counter-elements-integer-count-contract.md) · [Continue](collections-deque-append-to-collections-deque-rotate.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)

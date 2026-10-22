# hashlib — Creating hash objects

### Creating hash objects

Fresh hash objects come from calling constructor functions:

 hashlib.blake2b(*data=b''*, ***, *digest_size=64*, *key=b''*, *salt=b''*, *person=b''*, *fanout=1*, *depth=1*, *leaf_size=0*, *node_offset=0*, *node_depth=0*, *inner_size=0*, *last_node=False*, *usedforsecurity=True*)

 hashlib.blake2s(*data=b''*, ***, *digest_size=32*, *key=b''*, *salt=b''*, *person=b''*, *fanout=1*, *depth=1*, *leaf_size=0*, *node_offset=0*, *node_depth=0*, *inner_size=0*, *last_node=False*, *usedforsecurity=True*)

These functions give back the matching hash objects for computing BLAKE2b or BLAKE2s. Optionally they accept the following general parameters:

- *data*: opening block of data for hashing, required to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Only a positional argument may carry it.

- *digest_size*: the output digest’s size measured in bytes.

- *key*: the keyed-hashing key (up to 64 bytes for BLAKE2b, up to 32 bytes for BLAKE2s).

- *salt*: the randomized-hashing salt (up to 16 bytes for BLAKE2b, up to 8 bytes for BLAKE2s).

- *person*: the personalization string (BLAKE2b allows up to 16 bytes; BLAKE2s allows up to 8 bytes).

The table below lays out the limits for general parameters (in bytes):

| Hash | digest_size | len(key) | len(salt) | len(person) |
| --- | --- | --- | --- | --- |
| BLAKE2b | 64 | 64 | 16 | 16 |
| BLAKE2s | 32 | 32 | 8 | 8 |

Note

The BLAKE2 specification fixes constant lengths on the salt and personalization parameters; even so, as a convenience this implementation takes byte strings of any size up to the stated maximum. When a parameter falls short of the specified length, it is zero-padded, so that, for instance, `b'salt'` and `b'salt\x00'` come out as the same value. (That does not hold for *key*.)

These sizes are available as module constants described below.

Constructor functions also accept the following tree hashing parameters:

- *fanout*: the fanout value (0 to 255; use 0 for unlimited and 1 under sequential mode).

- *depth*: the tree’s greatest depth (1 to 255; use 255 for unlimited and 1 under sequential mode).

- *leaf_size*: a leaf’s greatest byte length (0 to `2**32-1`; use 0 for unlimited or under sequential mode).

- *node_offset*: the node offset (0 to `2**64-1` for BLAKE2b, 0 to `2**48-1` for BLAKE2s; use 0 for the leftmost, first leaf, or under sequential mode).

- *node_depth*: the node depth (0 to 255; use 0 for leaves or under sequential mode).

- *inner_size*: the inner digest size (0 to 64 for BLAKE2b, 0 to 32 for BLAKE2s; use 0 under sequential mode).

- *last_node*: a boolean flagging whether the node being processed is the final one (`False` under sequential mode).

  (Figure: Explanation of tree mode parameters.)

For an exhaustive treatment of tree hashing, refer to section 2.10 in [BLAKE2 specification](https://www.blake2.net/blake2_20130129.pdf).

[Subject index](INDEX.md) · [Previous](blake2.md) · [Continue](blake2b-salt-size-to-blake2s-max-digest-size.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)

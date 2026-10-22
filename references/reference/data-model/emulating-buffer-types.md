# 3.3.11. Emulating buffer types

### 3.3.11. Emulating buffer types

The [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) gives Python objects a means to expose efficient access to a low-level memory array. Builtin types like [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) implement this protocol, and third-party libraries may add further buffer types.

Although buffer types are commonly written in C, implementing the protocol in Python is also feasible.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](object-match-args.md) · [Following source section](object-buffer.md)

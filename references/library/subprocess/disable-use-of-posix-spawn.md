# subprocess — Disable use of `posix_spawn()`

### Disable use of `posix_spawn()`

Under Linux, whenever it is safe to do so, `subprocess` leans by default on the `vfork()` system call internally in place of `fork()`. Performance benefits substantially from this.

```python
subprocess._USE_POSIX_SPAWN = False  # See CPython issue gh-NNNNNN.

```

Setting this to false is harmless on any Python version; on older or newer ones where it is unsupported, it simply does nothing. Never presume the attribute can be read. The name notwithstanding, a true value does not promise that the matching function gets used — only that it might.

Whenever you find yourself reaching for these private knobs, please open an issue and include a way to reproduce what you ran into. From a comment in your own code, link back to that issue.

Added in version 3.8: `_USE_POSIX_SPAWN`

[Subject index](INDEX.md) · [Previous](converting-an-argument-sequence-to-a-string-on-windows.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

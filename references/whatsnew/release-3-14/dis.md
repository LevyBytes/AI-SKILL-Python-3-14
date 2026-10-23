# What's new in Python 3.14 / dis - dis

### dis

- Rendering the complete source location of [`instructions`](https://docs.python.org/3.14/library/dis.html#dis.Instruction) is now supported, going past merely the line number. The *show_positions* keyword argument brings this capability to these interfaces:

  - [`dis.Bytecode`](https://docs.python.org/3.14/library/dis.html#dis.Bytecode)

  - [`dis.dis()`](https://docs.python.org/3.14/library/dis.html#dis.dis)

  - [`dis.distb()`](https://docs.python.org/3.14/library/dis.html#dis.distb)

  - [`dis.disassemble()`](https://docs.python.org/3.14/library/dis.html#dis.disassemble)

The same capability is surfaced through [`dis --show-positions`](https://docs.python.org/3.14/library/dis.html#cmdoption-dis-P). (Contributed by Bénédikt Tran in [gh-123165](https://github.com/python/cpython/issues/123165).)

- The new [`dis --specialized`](https://docs.python.org/3.14/library/dis.html#cmdoption-dis-S) command-line option displays specialized bytecode. (Contributed by Bénédikt Tran in [gh-127413](https://github.com/python/cpython/issues/127413).)

[Subject index](INDEX.md) · [Previous source section](difflib.md) · [Next source section](errno.md) · [Release/subject declaration](summary-release-highlights.md)

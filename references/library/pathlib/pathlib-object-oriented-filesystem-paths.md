# pathlib — `pathlib` — Object-oriented filesystem paths

### `pathlib` — Object-oriented filesystem paths

Added in version 3.4.

**Source code:** [Lib/pathlib/](https://github.com/python/cpython/tree/3.14/Lib/pathlib/)

---

This module supplies classes that stand for filesystem paths, carrying semantics suited to the various operating systems. The path classes split into pure paths, which offer purely computational operations and no I/O, and concrete paths, which derive from pure paths yet additionally offer I/O operations.

 (Figure: Inheritance diagram showing the classes available in pathlib. The most basic class is PurePath, which has three direct subclasses: PurePosixPath, PureWindowsPath, and Path. Further to these four classes, there are two classes that use multiple inheritance: PosixPath subclasses PurePosixPath and Path, and WindowsPath subclasses PureWindowsPath and Path.)

When you have never touched this module before, or you simply are unsure which class fits your task, `Path` is most probably what you want. It builds a concrete path for the platform on which the code runs.

Pure paths come in handy in certain special situations; for instance:

1.

You want to manipulate Windows paths on a Unix machine (or the reverse). Running on Unix, you cannot instantiate a `WindowsPath`, yet you can instantiate `PureWindowsPath`.

2.

You want to be certain your code manipulates paths alone without ever touching the OS. Here, instantiating one of the pure classes can be useful, because those simply hold no OS-accessing operations.

See also

[**PEP 428**](https://peps.python.org/pep-0428/): The pathlib module – object-oriented filesystem paths.

See also

For low-level path manipulation on strings, the [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) module is available to you as well.

[Subject index](INDEX.md) · [Continue](basic-use.md)

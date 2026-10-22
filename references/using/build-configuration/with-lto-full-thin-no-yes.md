# --with-lto=[full/thin/no/yes]

--with-lto=[full|thin|no|yes]

Switch on Link Time Optimization (LTO) for any build (off by default).

For LTO the Clang C compiler needs `llvm-ar` (`ar` on macOS), together with a linker that understands LTO (`ld.gold` or `lld`).

Added in version 3.6.

Added in version 3.11: To use ThinLTO feature, use `--with-lto=thin` on Clang.

Changed in version 3.12: On Clang, when the compiler accepts the flag, ThinLTO becomes the default optimization policy.

[Subject index](INDEX.md) · [Previous source section](profile-task.md) · [Following source section](enable-bolt.md)

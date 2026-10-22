# --with-tail-call-interp

--with-tail-call-interp

Switch on interpreters that rely on tail calls inside CPython. When this is on, turning on PGO (`--enable-optimizations`) comes highly recommended. The option in particular demands a C compiler that has proper tail call support along with the [preserve_none](https://clang.llvm.org/docs/AttributeReference.html#preserve-none) calling convention. Clang 19 and newer, for instance, supports this feature.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source section](with-computed-gotos.md) · [Following source section](without-mimalloc.md)

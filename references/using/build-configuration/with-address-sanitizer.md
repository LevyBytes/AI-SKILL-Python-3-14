# --with-address-sanitizer

--with-address-sanitizer

Turn on the AddressSanitizer memory error detector, `asan` (off by default). For sharper ASan detection you might pair this with `--without-pymalloc`, which switches off the dedicated small-object allocator whose allocations ASan does not follow.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous source section](with-dtrace.md) · [Following source section](with-memory-sanitizer.md)

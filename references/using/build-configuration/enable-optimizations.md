# --enable-optimizations

--enable-optimizations

Switch on Profile Guided Optimization (PGO) by way of `PROFILE_TASK` (off by default).

For PGO, the Clang C compiler needs the `llvm-profdata` program. On macOS the same applies to GCC, since there GCC is merely an alias pointing to Clang.

Additionally switch off semantic interposition within libpython whenever `--enable-shared` is set and GCC is the compiler: append `-fno-semantic-interposition` onto the compiler and linker flags.

Note

As the build proceeds, the compiler may warn that profile data is unavailable for certain source files. Such warnings do no harm, because profile data acquisition exercises only part of the code. On Clang, you can silence these warnings by hand by appending `-Wno-profile-instr-unprofiled` onto `CFLAGS`.

Added in version 3.6.

Changed in version 3.10: Use `-fno-semantic-interposition` on GCC.

[Subject index](INDEX.md) · [Previous source section](performance-options.md) · [Following source section](profile-task.md)

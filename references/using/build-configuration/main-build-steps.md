# 3.4.2. Main build steps

### 3.4.2. Main build steps

- C files (`.c`) are built as object files (`.o`).

- A static `libpython` library (`.a`) gets assembled out of the object files.

- `python.o` together with the static `libpython` library get linked to form the final `python` program.

- The Makefile builds the C extensions (refer to `Modules/Setup`).

[Subject index](INDEX.md) · [Previous source section](main-files-of-the-build-system.md) · [Following source section](make.md)

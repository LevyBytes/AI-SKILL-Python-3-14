# 3.4.1. Main files of the build system

### 3.4. Python Build System

### 3.4.1. Main files of the build system

- `configure.ac` => `configure`;

- `Makefile.pre.in` => `Makefile` (created by `configure`);

- `pyconfig.h` (created by `configure`);

- `Modules/Setup`: C extensions that the Makefile builds by way of the `Module/makesetup` shell script;

[Subject index](INDEX.md) · [Previous source section](hostrunner.md) · [Following source section](main-build-steps.md)

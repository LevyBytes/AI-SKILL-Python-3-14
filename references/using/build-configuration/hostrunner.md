# HOSTRUNNER

HOSTRUNNER

Program that runs the host-platform CPython during cross-compilation.

Added in version 3.11.

A cross compiling sample:

```sh
CONFIG_SITE=config.site-aarch64 ../configure \
    --build=x86_64-pc-linux-gnu \
    --host=aarch64-unknown-linux-gnu \
    --with-build-python=../x86_64/python

```

[Subject index](INDEX.md) · [Previous source section](with-build-python-path-to-python.md) · [Following source section](main-files-of-the-build-system.md)

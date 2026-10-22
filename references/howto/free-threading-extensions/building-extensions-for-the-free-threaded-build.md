# Building Extensions for the Free-Threaded Build

### Building Extensions for the Free-Threaded Build

A C API extension has to be compiled expressly against the free-threaded build. You can spot the matching wheels, shared libraries, and binaries by their `t` suffix.

- [pypa/manylinux](https://github.com/pypa/manylinux) handles the free-threaded build and carries the `t` suffix, as in `python3.14t`.

- [pypa/cibuildwheel](https://github.com/pypa/cibuildwheel) can produce wheels targeting the free-threaded build from Python 3.14 onward.

[Subject index](INDEX.md) · [Previous source context](important-considerations.md) · [Following source context](limited-c-api-and-stable-abi.md)

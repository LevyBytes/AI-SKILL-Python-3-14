# Setup for Python from a Linux distro

### Setup for Python from a Linux distro

On the majority of Linux systems, debug information for the system Python arrives in a package named `python-debuginfo`, `python-dbg`, or something comparable. As an example:

- Fedora:

>

```shell
sudo dnf install gdb
sudo dnf debuginfo-install python3

```

- Ubuntu:

>

```shell
sudo apt install gdb python3-dbg

```

Across a number of current Linux systems, GDB is able to fetch debugging symbols on its own through *debuginfod*. That said, this leaves the `python-gdb.py` extension uninstalled; as a rule you still have to install the debug info package on its own.

[Subject index](INDEX.md) · [Previous source context](setup-with-python-built-from-source.md) · [Following source context](using-the-debug-build-and-development-mode.md)

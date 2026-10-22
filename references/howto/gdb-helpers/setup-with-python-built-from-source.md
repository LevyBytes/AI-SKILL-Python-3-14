# Setup with Python built from source

### Setup with Python built from source

Building CPython from source should make debugging information available, and the build ought to drop a `python-gdb.py` file into your repository's root directory.

Turning on support requires you to register the directory holding `python-gdb.py` with GDB's “auto-load-safe-path”. Should you have skipped this, current GDB versions will emit a warning telling you how to proceed.

Note

Where no instructions appear for your GDB version, drop this into your configuration file (`~/.gdbinit` or `~/.config/gdb/gdbinit`):

```none
add-auto-load-safe-path /path/to/cpython

```

Several paths may also be supplied, separated with `:`.

[Subject index](INDEX.md) · [Previous source context](prerequisites.md) · [Following source context](setup-for-python-from-a-linux-distro.md)

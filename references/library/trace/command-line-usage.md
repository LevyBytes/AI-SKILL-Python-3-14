# trace — Command-Line Usage

### Command-Line Usage

You can launch the `trace` module straight from the command line. In its simplest form that looks like

```python
python -m trace --count -C . somefile.py ...

```

That command runs `somefile.py` and drops annotated listings for every Python module imported while it ran into the current directory.

 --help

Show usage information, then quit.

 --version

Show the module's version, then quit.

Added in version 3.8: Introduced the `--module` option, which lets you run an executable module.

[Subject index](INDEX.md) · [Previous](coverage-py.md) · [Continue](main-options.md) · [Owning module, declaration or section: trace](coverage-py.md)

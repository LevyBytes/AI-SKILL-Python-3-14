# zipapp - Basic Example

### Basic Example

The example that follows demonstrates using the Command-Line Interface to turn a directory of Python code into an executable archive. Once launched, the archive runs the `main` function out of the `myapp` module held inside it.

```shell
$ python -m zipapp myapp -m "myapp:main"
$ python myapp.pyz
<output from myapp>

```

[Subject index](INDEX.md) · [Previous](zipapp-manage-executable-python-zip-archives.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)

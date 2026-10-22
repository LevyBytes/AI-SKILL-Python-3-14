# -X presite=*package.module*

`-X presite=*package.module*` names a module that gets imported ahead of the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module running and ahead of the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module coming into being. As a result, the module brought in is not `__main__`. You can leverage this to run code very early while Python is starting up. For this option to be present, Python must be [built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build). Refer also to `PYTHON_PRESITE`.

Added in version 3.13.

[Subject index](INDEX.md) · [Following source section](x-gil-0-1.md)

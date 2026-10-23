# sys.monitoring - _pth files

### _pth files

If you want to override [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) outright, create a `._pth` file whose name matches the executable or the shared library (`python._pth` or `python311._pth`). On Windows the shared library path is always known, though it may be unavailable on other platforms. Inside the `._pth` file, list one line per path you want added to `sys.path`. The file keyed to the shared library name takes precedence over the one keyed to the executable, which lets paths be locked down for any program that loads the runtime if that is what you want.

While the file exists, all registry and environment variables get ignored, isolated mode switches on, and [`site`](https://docs.python.org/3.14/library/site.html#module-site) goes unimported unless one line in the file says `import site`. Blank paths and lines beginning with `#` are skipped. Each path can be absolute or relative to where the file sits. Import statements other than to `site` are off-limits, and you cannot specify arbitrary code.

Be aware that `.pth` files (lacking the leading underscore) get processed in the usual way by the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module once `import site` has been specified.

[Subject index](INDEX.md) · [Previous](virtual-environments.md) · [Continue](embedded-python.md)

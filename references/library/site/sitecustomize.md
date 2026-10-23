# site`sitecustomize`

### `sitecustomize`

Once those path adjustments are done, Python tries to import a module called `sitecustomize`, a place for arbitrary site-specific customizations. A system administrator usually puts it in the site-packages directory. Should that import raise an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) (or a subclass) whose [`name`](https://docs.python.org/3.14/library/exceptions.html#ImportError.name) attribute is `'sitecustomize'`, the error is quietly swallowed. When Python runs with no output streams on hand — as happens with `pythonw.exe` on Windows, the default launcher for IDLE — any output `sitecustomize` tries to emit is discarded. Any other exception brings about a silent, possibly baffling, failure of the process.

[Subject index](INDEX.md) · [Previous](site-site-specific-configuration-hook.md) · [Continue](usercustomize.md) · [Owning module, declaration or section: site](site-site-specific-configuration-hook.md)

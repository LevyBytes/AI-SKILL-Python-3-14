# site`usercustomize`

### `usercustomize`

Following that, provided `ENABLE_USER_SITE` is true, Python attempts to import a module called `usercustomize`, which exists for arbitrary user-specific customizations. The intent is for this file to live in the user site-packages directory (described below), a member of `sys.path` unless turned off with [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s). If the import throws an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) (or a subclass) carrying a [`name`](https://docs.python.org/3.14/library/exceptions.html#ImportError.name) attribute of `'usercustomize'`, it is quietly disregarded.

Bear in mind that on certain non-Unix systems `sys.prefix` and `sys.exec_prefix` come out empty, so the path manipulations are bypassed; even then, Python still tries to import `sitecustomize` and `usercustomize`.

[Subject index](INDEX.md) · [Previous](sitecustomize.md) · [Continue](readline-configuration.md) · [Owning module, declaration or section: site](site-site-specific-configuration-hook.md)

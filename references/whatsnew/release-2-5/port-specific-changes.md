# What's New in Python 2.5 / Port-Specific Changes

### Port-Specific Changes

- MacOS X (10.3 and higher): modules are now dynamically loaded through the `dlopen()` function rather than the MacOS-specific calls used before.

- MacOS X: the **configure** script gained an `--enable-universalsdk` option that builds the interpreter as a universal binary capable of executing on PowerPC as well as Intel chips. (Contributed by Ronald Oussoren; [bpo-2573](https://bugs.python.org/issue?@action=redirect&bpo=2573).)

- Windows: the `.dll` suffix is no longer accepted as a filename extension for extension modules; from now on only `.pyd` will be looked for.

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Next source section](porting-to-python-2-5.md) · [Release/subject declaration](pep-308-conditional-expressions.md)

# Python 3.7.0 beta 5 / core and builtins / removed

[bpo-20104](https://bugs.python.org/issue?@action=redirect&bpo=20104): The fresh `os.posix_spawn` introduced in 3.7.0b1 got removed since we're still deciding what the API ought to be. Look for it in 3.8 instead.

[bpo-32911](https://bugs.python.org/issue?@action=redirect&bpo=32911): Owing to surprise compatibility problems surfacing during downstream beta testing, [bpo-29463](https://bugs.python.org/issue?@action=redirect&bpo=29463) was reverted. The `docstring` field, added in 3.7a1, is removed from the Module, ClassDef, FunctionDef, and AsyncFunctionDef ast nodes. Their body once again carries the docstring expression as a first statement. Based on a patch from Inada Naoki.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

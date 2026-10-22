# test.support.os_helper: `test.support.os_helper.FakePath`, `EnvironmentVarGuard.set()`, `EnvironmentVarGuard.unset()`

*class *test.support.os_helper.FakePath(*path*)

A basic [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). It supplies the [`__fspath__()`](https://docs.python.org/3.14/library/os.html#os.PathLike.__fspath__) method, which merely returns the *path* argument. When *path* is an exception, that exception is raised within `__fspath__()`.

 EnvironmentVarGuard.set(*envvar*, *value*)

Temporarily assigns the environment variable `envvar` the value `value`.

 EnvironmentVarGuard.unset(*envvar*, **others*)

Temporarily clears one or more environment variables.

Changed in version 3.14: Unsetting several environment variables at once is now supported.

[Subject index](INDEX.md) · [Previous](test-support-os-helper-environmentvarguard-class.md) · [Continue](os-test-symlink-and-directory-helpers.md) · [Owning module, declaration or section: test.support.os_helper](filesystem-encoding-test-names.md)

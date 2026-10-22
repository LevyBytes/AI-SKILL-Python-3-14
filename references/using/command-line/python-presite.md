# PYTHON_PRESITE

PYTHON_PRESITE

Point this variable at a module and that module gets imported very early in the interpreter's lifetime — ahead of running the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module and ahead of building the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module. Because of that ordering, the module you import is never regarded as `__main__`.

It offers a way to run your own code right at the start of Python initialization.

For a submodule, supply `package.module` as the value, just as you would inside an import statement.

Refer as well to the `-X presite` command-line option, which overrides this variable.

Requires a Python built using the [`--with-pydebug`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-pydebug) build option.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous source section](pythondumprefsfile.md)

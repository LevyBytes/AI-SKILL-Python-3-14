# subprocess - Replacing Older Functions with the `subprocess` Module

### Replacing Older Functions with the `subprocess` Module

Throughout this section, the phrase “a becomes b” signals that b serves as a stand-in for a.

Note

Every “a” function covered here fails more or less quietly when the program being run cannot be located; the “b” stand-ins raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) in that situation instead.

On top of that, the stand-ins built on `check_output()` fail with a `CalledProcessError` whenever the requested operation yields a non-zero return code. Even so, the output remains reachable through the `output` attribute of the exception that was raised.

For the examples below, take it as given that the pertinent functions have already been imported out of the `subprocess` module.

[Subject index](INDEX.md) · [Previous](subprocess-check-output.md) · [Continue](replacing-bin-sh-shell-command-substitution.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

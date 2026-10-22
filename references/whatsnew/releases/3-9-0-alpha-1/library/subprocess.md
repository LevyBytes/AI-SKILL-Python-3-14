# Python 3.9.0 alpha 1 / library / subprocess

[bpo-34886](https://bugs.python.org/issue?@action=redirect&bpo=34886): Cleared an accidental ValueError out of [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) that appeared while it checked for clashing *input* and *stdin*, or *capture_output* and *stdout* or *stderr* arguments, in the case where those were supplied explicitly yet with `None` values inside a passed-in `**kwargs` dict rather than handed straight in by name. Rémi Lapeyre contributed the patch.

[bpo-38417](https://bugs.python.org/issue?@action=redirect&bpo=38417): On POSIX systems, the subprocess module gained the ability to set the umask of the child process.

[bpo-37951](https://bugs.python.org/issue?@action=redirect&bpo=37951): Within subinterpreters, most of the subprocess module's capabilities work once more. The single restriction in subinterpreters concerns *preexec_fn*.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

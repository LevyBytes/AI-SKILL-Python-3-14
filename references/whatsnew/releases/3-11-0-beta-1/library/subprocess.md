# Python 3.11.0 beta 1 / library / subprocess

[gh-92301](https://github.com/python/cpython/issues/92301): Within [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess), favor `close_range()` over walking procfs when closing file descriptors, which performs better.

[gh-91954](https://github.com/python/cpython/issues/91954): Give [`subprocess.getoutput()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.getoutput) and [`subprocess.getstatusoutput()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.getstatusoutput) the *encoding* and *errors* arguments.

[gh-91401](https://github.com/python/cpython/issues/91401): Offer a means to switch off [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) usage of `vfork()` should that ever become necessary, and document the already-existing mechanism covering `posix_spawn()`.

[bpo-38435](https://bugs.python.org/issue?@action=redirect&bpo=38435): Give [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) a `process_group` parameter so that more functionality can migrate away from the risky `preexec_fn` parameter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

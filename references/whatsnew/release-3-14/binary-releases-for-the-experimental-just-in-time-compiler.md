# What's new in Python 3.14 / Binary releases for the experimental just-in-time compiler - pdb, profile, sys

### Binary releases for the experimental just-in-time compiler

An *experimental* just-in-time (JIT) compiler now ships inside the official macOS and Windows release binaries. While it is **not** advised for production deployments, you can exercise it by setting the environment variable [`PYTHON_JIT=1`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_JIT). Source builds downstream and redistributors may apply the [`--enable-experimental-jit=yes-off`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-experimental-jit) configuration option to get comparable behavior.

Still under active development, the JIT remains early-stage. Consequently, switching it on can shift typical performance anywhere from 10% slower to 20% faster, varying by workload. For testing and evaluation purposes, several introspection functions live in the [`sys._jit`](https://docs.python.org/3.14/library/sys.html#sys._jit) namespace. Call [`sys._jit.is_available()`](https://docs.python.org/3.14/library/sys.html#sys._jit.is_available) to check whether the running executable can compile via JIT, and [`sys._jit.is_enabled()`](https://docs.python.org/3.14/library/sys.html#sys._jit.is_enabled) to learn whether JIT compilation is turned on for the active process.

At the moment, the largest gap is that native debuggers and profilers such as `gdb` and `perf` cannot unwind across JIT frames (Python-level debuggers and profilers, such as [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) or [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile), keep working unchanged). JIT compilation is unavailable on free-threaded builds.

Do report any bugs or serious performance regressions you run into!

See also

[**PEP 744**](https://peps.python.org/pep-0744/)

[Subject index](INDEX.md) · [Previous source section](free-threaded-python-is-officially-supported.md) · [Next source section](porting-to-python-3-14.md) · [Release/subject declaration](summary-release-highlights.md)

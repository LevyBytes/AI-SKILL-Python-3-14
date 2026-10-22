# What’s New In Python 3.8 / Debug build uses the same ABI as release build — sys

### Debug build uses the same ABI as release build

Python [debug builds](https://docs.python.org/3.14/using/configure.html#debug-build) now carry an ABI that matches Python release builds. On Unix, a Python compiled in debug mode can now load both C extensions compiled in release mode and C extensions compiled against the stable ABI. Going the other direction does not work, because debug builds publish extra symbols that release builds lack.

Setting the `Py_DEBUG` macro no longer drags in the `Py_TRACE_REFS` macro, and that dependency was the sole source of ABI incompatibility. The `Py_TRACE_REFS` macro — which supplies the [`sys.getobjects()`](https://docs.python.org/3.14/library/sys.html#sys.getobjects) function plus the [`PYTHONDUMPREFS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDUMPREFS) environment variable — can instead be enabled through the new [`./configure --with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs) build option. (Victor Stinner contributed this in [bpo-36465](https://bugs.python.org/issue?@action=redirect&bpo=36465).)

On Unix, C extensions stop linking against libpython, with Android and Cygwin as the two exceptions. A statically linked Python can now load a C extension that was built against a shared-library Python. (Victor Stinner contributed this in [bpo-21536](https://bugs.python.org/issue?@action=redirect&bpo=21536).)

On Unix, with Python built in debug mode, import will henceforth also seek out release-mode-compiled C extensions as well as those built against the stable ABI. (Victor Stinner contributed this in [bpo-36722](https://bugs.python.org/issue?@action=redirect&bpo=36722).)

When you embed Python inside an application, a new `--embed` flag has to be handed to `python3-config --libs --embed` so that you receive `-lpython3.8` (which links the application against libpython). If you need to cover both 3.8 and earlier, attempt `python3-config --libs --embed` first, and drop back to `python3-config --libs` (no `--embed`) whenever that earlier command errors out.

There is also a new pkg-config `python-3.8-embed` module for embedding Python in an application: `pkg-config python-3.8-embed --libs` brings in `-lpython3.8`. To handle 3.8 alongside older releases, try `pkg-config python-X.Y-embed --libs` first and fall back to `pkg-config python-X.Y --libs` (no `--embed`) if that first attempt fails (substitute the Python version for `X.Y`).

Meanwhile, `pkg-config python3.8 --libs` no longer carries `-lpython3.8`. C extensions are not supposed to link against libpython — Android and Cygwin remain special cases the script handles — and this break with the past was made deliberately. (Victor Stinner contributed this in [bpo-36721](https://bugs.python.org/issue?@action=redirect&bpo=36721).)

[Subject index](INDEX.md) · [Previous source section](parallel-filesystem-cache-for-compiled-bytecode-files.md) · [Next source section](fstring-debug-expressions.md) · [Release/subject declaration](assignment-expressions.md)

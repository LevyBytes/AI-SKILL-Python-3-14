# sys.monitoring — The initialization of the `sys.path` module search path

## The initialization of the sys.path module search path

### The initialization of the [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) module search path

When Python launches, a module search path gets initialized. You can reach this module search path at [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

The module search path's first entry is the directory holding the input script, when one exists. If not, the first entry is the working directory, as happens when you run the interactive shell, a [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) command, or [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) module.

Adding directories to the search path is commonly handled with the [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) environment variable. When this environment variable is present, its contents get appended to the module search path.

Note

Every installed Python version/environment feels the effect of [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH). Think twice before placing it in your shell profile or among global environment variables. The [`site`](https://docs.python.org/3.14/library/site.html#module-site) module, covered further down, supplies more nuanced approaches.

What gets added next are the directories that hold the standard Python modules together with any [extension module](https://docs.python.org/3.14/glossary.html#term-extension-module)s those modules rely on. Extension modules come as `.pyd` files on Windows and `.so` files elsewhere. The directory carrying the platform-independent Python modules goes by `prefix`. The directory carrying the extension modules goes by `exec_prefix`.

You may set the `prefix` and `exec_prefix` locations through the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable. Failing that, these directories are located by taking the Python executable as a jumping-off point and then scanning for assorted 'landmark' files and directories. Note that any symbolic links get followed, so the actual Python executable location serves as the search starting point. That Python executable location goes by `home`.

With `home` established, the `prefix` directory is located by first scanning for `python*majorversion**minorversion*.zip` (`python311.zip`). On Windows the zip archive is sought in `home`, while on Unix the archive is looked for in `lib`. Note that the expected zip archive location joins the module search path even when the archive is absent. Where no archive turned up, Python on Windows carries on hunting for `prefix` by scanning for `Lib\os.py`. Python on Unix will scan for `lib/python*majorversion*.*minorversion*/os.py` (`lib/python3.11/os.py`). On Windows `prefix` and `exec_prefix` coincide, whereas on other platforms `lib/python*majorversion*.*minorversion*/lib-dynload` (`lib/python3.11/lib-dynload`) is sought out and used as an anchor for `exec_prefix`. On certain platforms `lib` may instead be `lib64` or some other value; see [`sys.platlibdir`](https://docs.python.org/3.14/library/sys.html#sys.platlibdir) and [`PYTHONPLATLIBDIR`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPLATLIBDIR).

After they are located, `prefix` and `exec_prefix` become available at [`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix) and [`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix) respectively.

When [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) is unset and a `pyvenv.cfg` file turns up beside the main executable, or in its parent directory, [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) and [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) get pointed at the directory holding `pyvenv.cfg`; otherwise they get pointed at the same value as [`sys.base_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_prefix) and [`sys.base_exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.base_exec_prefix), respectively. Virtual Environments rely on this.

Last of all, the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module gets processed and `site-packages` directories join the module search path. One common way to tailor the search path is to write [`sitecustomize`](https://docs.python.org/3.14/library/site.html#module-sitecustomize) or [`usercustomize`](https://docs.python.org/3.14/library/site.html#module-usercustomize) modules as the `site` module documentation describes.

Note

A handful of command line options can shape path calculations even more. For the particulars, see [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E), [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I), [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s) and [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S).

Changed in version 3.14: [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) and [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) now get pointed at the `pyvenv.cfg` directory while the path is initialized. That used to be the job of [`site`](https://docs.python.org/3.14/library/site.html#module-site), and so was subject to [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S).

[Subject index](INDEX.md) · [Continue](virtual-environments.md)

# 4.8. Finding modules

### 4.8. Finding modules

The following notes add Windows-specific detail to the account given at [The initialization of the sys.path module search path](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init).

In the absence of a `._pth` file, [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) gets filled out on Windows in this manner:

- A blank entry is placed at the front, standing in for the current directory.

- When the environment variable [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) is present, as covered in [Environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-envvars), its entries come next. Be aware that on Windows, the paths within this variable have to be split by semicolons, so they stay distinct from the colon found in drive identifiers (`C:\` etc.).

- Further "application paths" may be registered as subkeys of `\SOFTWARE\Python\PythonCore{version}\PythonPath` beneath both the `HKEY_CURRENT_USER` and `HKEY_LOCAL_MACHINE` hives. Any subkey whose default value is a semicolon-delimited path string causes each of those paths to land in [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). (Bear in mind that every known installer touches only HKLM, so HKCU is usually empty.)

- When the environment variable [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) has a value, that value is taken as the "Python Home". If it does not, the location of the main Python executable is used to track down a "landmark file" (either `Lib\os.py` or `pythonXY.zip`) and from there infer the "Python Home". Once a Python home turns up, the matching sub-directories that get appended to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) (`Lib`, `plat-win`, etc) derive from that folder. If not, the core Python path comes from the PythonPath kept in the registry.

- When the Python Home cannot be pinned down, no [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) appears in the environment, and no registry entries surface, a default path made of relative entries is applied (for example `.\Lib;.\plat-win`, etc).

When a `pyvenv.cfg` file turns up next to the main executable, or in the directory one level above it, these adjustments take effect:

- When `home` holds an absolute path and [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) has no value, that path replaces the path to the main executable for the purpose of working out the home location.

Here is what all of this ultimately produces:

- While running `python.exe`, or any other .exe inside the main Python directory (whether an installed copy or one straight from the PCbuild directory), the core path is inferred and the registry core paths are skipped. Other registry "application paths" are read every time.

- When another .exe hosts Python (a different directory, embedded by way of COM, and so on), the "Python Home" goes uninferred, so the core path from the registry applies. Other registry "application paths" are read every time.

- When Python can't locate its home and no registry value exists (a frozen .exe, some highly unusual installation setup), you end up with a path built from certain default, yet relative, paths.

If you intend to package Python inside your own application or distribution, the guidance below helps you steer clear of clashes with other installations:

- Ship a `._pth` file beside your executable that lists the directories to bring in. Doing so disregards paths held in the registry and environment variables, and also disregards [`site`](https://docs.python.org/3.14/library/site.html#module-site) unless `import site` appears in it.

- When your own executable loads `python3.dll` or `python37.dll`, assign [`PyConfig.module_search_paths`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.module_search_paths) explicitly ahead of [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig).

- Wipe and/or replace [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH) and assign [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) before your application starts `python.exe`.

- When none of the preceding suggestions works for you (say, you are a distribution that lets people invoke `python.exe` directly), make sure the landmark file (`Lib\os.py`) is present in your install directory. (Bear in mind it goes undetected inside a ZIP file, though a properly named ZIP file is detected in its place.)

Together these steps guarantee that a system-wide installation's files won't win out over the standard library copy you ship with your application. Without them, your users could run into trouble running your application. Note that the first suggestion stands as the strongest, because the rest can still be tripped up by non-standard paths in the registry and user site-packages.

Changed in version 3.6: Add `._pth` file support and removes `applocal` option from `pyvenv.cfg`.

Changed in version 3.6: Treat `python*XX*.zip` as a possible landmark whenever it sits right beside the executable.

Deprecated since version 3.6: Any modules listed in the registry beneath `Modules` (rather than `PythonPath`) can be brought in by [`importlib.machinery.WindowsRegistryFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.WindowsRegistryFinder). On Windows this finder ships enabled in 3.6.0 and prior, yet down the road you might have to add it to [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) by hand.

[Subject index](INDEX.md) · [Previous source section](utf-8-mode.md) · [Following source section](additional-modules.md)

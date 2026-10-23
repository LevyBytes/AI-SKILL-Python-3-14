# modulefinder: `modulefinder.AddPackagePath()`, `modulefinder.ReplacePackage()`

## modulefinder - Find modules used by a script

### `modulefinder` - Find modules used by a script

**Source code:** [Lib/modulefinder.py](https://github.com/python/cpython/tree/3.14/Lib/modulefinder.py)

---

A `ModuleFinder` class is supplied by this module for working out which modules a script imports. You can also run `modulefinder.py` itself as a script — pass the path of a Python script as its argument, and it prints a report listing the imported modules.

 modulefinder.AddPackagePath(*pkg_name*, *path*)

Note that the package called *pkg_name* is located at the given *path*.

 modulefinder.ReplacePackage(*oldname*, *newname*)

Lets you state that the module called *oldname* is actually the package called *newname*.

[Subject index](INDEX.md) · [Continue](module-finder-analysis-and-script-execution.md)

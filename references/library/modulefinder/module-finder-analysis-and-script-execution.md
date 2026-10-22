# modulefinder / Find modules used by a script: `modulefinder.ModuleFinder`, `report()`, `run_script()`

*class *modulefinder.ModuleFinder(*path=None*, *debug=0*, *excludes=[]*, *replace_paths=[]*)

The `run_script()` and `report()` methods of this class work out which modules a script imports. A list of directories to search for modules may be passed as *path*; if it is omitted, `sys.path` serves instead. The *debug* argument sets the debugging level, and raising it makes the class emit more debugging messages about its activity. A list of module names to leave out of the analysis is given as *excludes*. The *replace_paths* argument is a list of `(oldpath, newpath)` tuples to be substituted within module paths.

 report()

Write a report to standard output listing the modules the script imports along with their paths, plus modules that are missing or appear to be missing.

 run_script(*pathname*)

Analyze the contents of the *pathname* file, which must contain Python code.

 modules

A dictionary mapping module names to modules. See Example usage of ModuleFinder.

[Subject index](INDEX.md) · [Previous](modulefinder-addpackagepath-to-modulefinder-replacepackage.md) · [Continue](example-usage-of-modulefinder.md) · [Owning module, declaration or section: modulefinder](modulefinder-addpackagepath-to-modulefinder-replacepackage.md)

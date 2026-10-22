# compileall: `compileall.compile_dir()`, `compileall.compile_file()`

### Public functions

 `compileall.compile_dir(*dir*, *maxlevels=sys.getrecursionlimit()*, *ddir=None*, *force=False*, *rx=None*, *quiet=0*, *legacy=False*, *optimize=-1*, *workers=1*, *invalidation_mode=None*, ***, *stripdir=None*, *prependdir=None*, *limit_sl_dest=None*, *hardlink_dupes=False*)`

Walk the directory tree designated by *dir* recursively, compiling every `.py` file encountered. Yield a true value when all files compiled without trouble, otherwise a false value.

The depth of the recursion is capped by the *maxlevels* parameter, whose default is `sys.getrecursionlimit()`.

When *ddir* is supplied, it goes in front of the path of each compiled file for the benefit of compilation-time tracebacks, and it is likewise embedded in the byte-code file, where it feeds tracebacks and other messages whenever the source file is gone by the time the byte-code executes.

A true *force* triggers re-compilation of modules even when their timestamps are already current.

When *rx* is supplied, its `search` method runs against the full path of every file under consideration, and any file for which it returns a true value is left out. This lets you exclude files that match a regular expression, supplied as a [re.Pattern](https://docs.python.org/3.14/library/re.html#re-objects) object.

When *quiet* is `False` or `0` (the default), filenames and related details go to standard out. At `1`, only errors appear. At `2`, all output is held back.

A true *legacy* writes byte-code files at their legacy paths and names, possibly clobbering byte-code files from a different Python version. By default the files go to their [**PEP 3147**](https://peps.python.org/pep-3147/) paths and names, letting byte-code from multiple Python versions coexist.

*optimize* sets the compiler's optimization level. It is handed to the built-in [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) function. It also accepts a sequence of optimization levels, yielding several compilations of a single `.py` file within one call.

How many workers compile files concurrently is governed by the *workers* argument. By default no multiple workers are used. Should the platform be unable to use multiple workers while a *workers* argument is supplied, it falls back to sequential compilation. A *workers* value of 0 selects the machine's core count. A *workers* value below `0` raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

*invalidation_mode* ought to be one of the [`py_compile.PycInvalidationMode`](https://docs.python.org/3.14/library/py_compile.html#py_compile.PycInvalidationMode) enum members and dictates how the produced pycs get invalidated while running.

The *stripdir*, *prependdir* and *limit_sl_dest* arguments line up with the `-s`, `-p` and `-e` options covered earlier. Each may be given as `str` or [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike).

When *hardlink_dupes* is true and two `.pyc` files at differing optimization levels share identical content, hard links merge the duplicate files.

Changed in version 3.2: Added the *legacy* and *optimize* parameter.

Changed in version 3.5: Added the *workers* parameter.

Changed in version 3.5: The *quiet* parameter turned into a multilevel value.

Changed in version 3.5: Regardless of what *optimize* is set to, the *legacy* parameter emits only `.pyc` files and never `.pyo` ones.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: The *invalidation_mode* parameter was added.

Changed in version 3.7.2: The default for the *invalidation_mode* parameter became `None`.

Changed in version 3.8: A *workers* value of 0 now picks the ideal core count.

Changed in version 3.9: Brought in the *stripdir*, *prependdir*, *limit_sl_dest* and *hardlink_dupes* arguments. The default for *maxlevels* moved from `10` over to `sys.getrecursionlimit()`

 `compileall.compile_file(*fullname*, *ddir=None*, *force=False*, *rx=None*, *quiet=0*, *legacy=False*, *optimize=-1*, *invalidation_mode=None*, ***, *stripdir=None*, *prependdir=None*, *limit_sl_dest=None*, *hardlink_dupes=False*)`

Compile the single file located at *fullname*. Hand back a true value when that file compiled cleanly, and a false value if not.

When *ddir* is supplied, it precedes the path of the file being compiled so compilation-time tracebacks can use it, and it is also stored inside the byte-code file, where tracebacks and other messages draw on it whenever the source file is absent at the moment the byte-code runs.

When *rx* is supplied, its `search` method receives the full path name of the file being compiled, and a true return leaves the file uncompiled while `True` comes back. This serves to skip files matching a regular expression, given as a [re.Pattern](https://docs.python.org/3.14/library/re.html#re-objects) object.

When *quiet* is `False` or `0` (the default), filenames and related details go to standard out. At `1`, only errors appear. At `2`, all output is held back.

A true *legacy* writes byte-code files at their legacy paths and names, possibly clobbering byte-code files from a different Python version. By default the files go to their [**PEP 3147**](https://peps.python.org/pep-3147/) paths and names, letting byte-code from multiple Python versions coexist.

*optimize* sets the compiler's optimization level. It is handed to the built-in [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) function. It also accepts a sequence of optimization levels, yielding several compilations of a single `.py` file within one call.

*invalidation_mode* ought to be one of the [`py_compile.PycInvalidationMode`](https://docs.python.org/3.14/library/py_compile.html#py_compile.PycInvalidationMode) enum members and dictates how the produced pycs get invalidated while running.

The *stripdir*, *prependdir* and *limit_sl_dest* arguments line up with the `-s`, `-p` and `-e` options covered earlier. Each may be given as `str` or [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike).

When *hardlink_dupes* is true and two `.pyc` files at differing optimization levels share identical content, hard links merge the duplicate files.

Added in version 3.2.

Changed in version 3.5: The *quiet* parameter was promoted to a multilevel value.

Changed in version 3.5: No matter how *optimize* is set, the *legacy* parameter produces `.pyc` files only and skips `.pyo` files entirely.

Changed in version 3.7: The *invalidation_mode* parameter was added.

Changed in version 3.7.2: For the *invalidation_mode* parameter, the default was revised to `None`.

Changed in version 3.9: Added *stripdir*, *prependdir*, *limit_sl_dest* and *hardlink_dupes* arguments.

[Subject index](INDEX.md) · [Previous](command-line-use.md) · [Continue](compileall-compile-path.md) · [Owning module, declaration or section: compileall](compileall-byte-compile-python-libraries.md)

# What's New In Python 3.2 / PEP 3147: PYC Repository Directories — compileall, importlib, py_compile

### PEP 3147: PYC Repository Directories

The approach Python used for stashing bytecode in *.pyc* files behaved poorly wherever several Python interpreters coexisted. Should one interpreter come across a cache produced by a different one, it would recompile the source and clobber the cache, forfeiting whatever caching had gained.

So-called "pyc fights" grew more visible as shipping several Python versions in a single Linux distribution turned routine. Such clashes also surface with CPython alternatives like Unladen Swallow.

The fix extended Python's import machinery so that each interpreter writes uniquely named files. Rather than Python 3.2, Python 3.3, and Unladen Swallow all contending over one file named "mymodule.pyc", each now seeks "mymodule.cpython-32.pyc", "mymodule.cpython-33.pyc", and "mymodule.unladen10.pyc". So that this crop of new files does not litter source directories, the *pyc* files now gather inside a "__pycache__" directory kept beneath the package directory.

Beyond the renaming and relocation, a few facets of the new arrangement are observable to the programmer:

- A module that has been imported now carries a [`__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__) attribute recording the name of the file that was actually imported:

```python
>>> import collections
>>> collections.__cached__
'c:/py32/lib/__pycache__/collections.cpython-32.pyc'

```

- Each interpreter's distinguishing tag can be read out of the `imp` module:

```python
>>> import imp
>>> imp.get_tag()
'cpython-32'

```

- Code that attempts to work back to a source filename from an imported file now has to be more careful. Merely dropping the "c" off a ".pyc" name no longer cuts it. Reach instead for the new helpers in the `imp` module:

```python
>>> imp.source_from_cache('c:/py32/lib/__pycache__/collections.cpython-32.pyc')
'c:/py32/lib/collections.py'
>>> imp.cache_from_source('c:/py32/lib/collections.py')
'c:/py32/lib/__pycache__/collections.cpython-32.pyc'

```

- Both the [`py_compile`](https://docs.python.org/3.14/library/py_compile.html#module-py_compile) and [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) modules were revised to honor the renamed files and relocated directory. Running *compileall* from the command line now accepts fresh options: `-i` names a list of files and directories to compile, while `-b` directs bytecode files to their old-style spot instead of *__pycache__*.

- The [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) module picked up new [abstract base classes](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) for loading bytecode files. The stale ABCs, `PyLoader` and `PyPycLoader`, are now deprecated (the documentation explains how to remain Python 3.1 compatible).

See also

[**PEP 3147**](https://peps.python.org/pep-3147/) - PYC Repository Directories

PEP written by Barry Warsaw.

[Subject index](INDEX.md) · [Previous source section](pep-3148-the-concurrent-futures-module.md) · [Next source section](pep-3149-abi-version-tagged-so-files.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

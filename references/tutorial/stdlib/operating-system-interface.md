# 10.1. Operating system interface

# Stdlib

### 10. Brief tour of the standard library

### 10.1. Operating system interface

For talking to the operating system, the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module hands you dozens of functions:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python314'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0

```

Favor the `import os` form over `from os import *`. Doing so prevents [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) from masking the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open), whose behavior differs considerably.

When you are exploring sizeable modules such as [`os`](https://docs.python.org/3.14/library/os.html#module-os) interactively, the built-in [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) and [`help()`](https://docs.python.org/3.14/library/functions.html#help) functions come in handy:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>

```

To handle everyday file and directory chores, the [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module offers a friendlier, higher-level interface:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'

```

[Subject index](INDEX.md) · [Following source section](file-wildcards.md)

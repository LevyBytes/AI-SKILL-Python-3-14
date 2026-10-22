# 6.2. Standard Modules

### 6.2. Standard Modules

Python ships with a collection of standard modules, documented separately in the Python Library Reference (the "Library Reference" from here on). A handful of modules are built straight into the interpreter; these expose operations that aren't part of the language's core but are nonetheless built in—either for the sake of efficiency or to reach operating-system primitives like system calls. Which modules belong to this set is a configuration choice that also hinges on the underlying platform. For instance, the [`winreg`](https://docs.python.org/3.14/library/winreg.html#module-winreg) module ships only on Windows systems. One module is worth a closer look: [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys), present in every Python interpreter. The variables `sys.ps1` and `sys.ps2` hold the strings used for the primary and secondary prompts:

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

```

Those two variables exist only when the interpreter runs in interactive mode.

The variable `sys.path` is a list of strings that sets the interpreter's search path for modules. Its default value comes from the environment variable [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH), or from a built-in default when `PYTHONPATH` isn't set. You're free to change it with ordinary list operations:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

```

[Subject index](INDEX.md) · [Previous source section](compiled-python-files.md) · [Following source section](the-dir-function.md)

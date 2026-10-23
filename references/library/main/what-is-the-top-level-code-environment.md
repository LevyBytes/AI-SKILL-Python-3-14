# __main__ - What is the “top-level code environment”?

### What is the “top-level code environment”?

`__main__` denotes the environment in which top-level code executes. By "top-level code" we mean the first user-chosen Python module to begin running. The label "top-level" fits because it pulls in every other module the program relies on. On occasion, "top-level code" is referred to as an *entry point* to the application.

A top-level code environment may take any of these forms:

- the scope belonging to an interactive prompt:

```python
>>> __name__
'__main__'

```

- the Python module handed to the Python interpreter as a file argument:

```shell
$ python helloworld.py
Hello, world!

```

- the Python module or package given to the Python interpreter through the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) argument:

```shell
$ python -m tarfile
usage: tarfile.py [-h] [-v] (...)

```

- Python code the Python interpreter reads off standard input:

```shell
$ echo "import this" | python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

```

- Python code supplied to the Python interpreter via the [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) argument:

```shell
$ python -c "import this"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

```

Across every one of these cases, the top-level module's `__name__` ends up as `'__main__'`.

Consequently, a module can tell whether it is the one running at top level by inspecting its own `__name__`, which underpins a familiar idiom for running code only when the module was not brought in through an import statement:

```python
if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    ...

```

See also

For a closer examination of how `__name__` gets assigned in every scenario, consult the tutorial section [Modules](https://docs.python.org/3.14/tutorial/modules.html#tut-modules).

[Subject index](INDEX.md) · [Previous](name-main.md) · [Continue](idiomatic-usage.md) · [Owning module, declaration or section: __main__](main-top-level-code-environment.md)

# unittest — Command-Line Interface

### Command-Line Interface

You can drive the unittest module from the command line to run tests sourced from modules, from classes, or even from individual test methods:

```python
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

```

Feel free to pass a list mixing module names together with fully qualified class or method names in any combination.

You can also name test modules by file path:

```python
python -m unittest tests/test_something.py

```

Doing so lets the shell's filename completion help you name the test module. Even then, the file you name has to be importable as a module. To produce the module name, the path has the '.py' stripped off and its path separators swapped for '.'. Should you wish to run a test file that cannot be imported as a module, run the file directly instead.

Pass the -v flag to get more detail (higher verbosity) when running tests:

```python
python -m unittest -v test_module

```

Running it with no arguments kicks off Test Discovery:

```python
python -m unittest

```

To see every one of the command-line options:

```python
python -m unittest -h

```

Changed in version 3.2: Prior releases allowed running only individual test methods, never whole modules or classes.

Added in version 3.14: By default the output now carries color, which you can [control using environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color).

[Subject index](INDEX.md) · [Previous](basic-example.md) · [Continue](command-line-options.md) · [Owning module, declaration or section: unittest](unittest-unit-testing-framework.md)

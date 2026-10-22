# doctest: Doctest debugger integration

### Debugging

For debugging doctest examples, doctest offers a handful of mechanisms:

- A number of functions turn doctests into runnable Python programs that you can then step through with the Python debugger, [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb).

- A subclass of `DocTestRunner`, the `DebugRunner` class throws an exception at the very first example that fails, carrying details about that example. Those details let you carry out post-mortem debugging on it.

- Those [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) cases that `DocTestSuite()` produces carry the `debug()` method that [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) defines.

- Drop a call to [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace) into a doctest example and, the moment that line runs, you land in the Python debugger, free to look over the present values of variables and the like. To illustrate, imagine `a.py` holds nothing but this module docstring:

```python
"""
>>> def f(x):
...     g(x*2)
>>> def g(x):
...     print(x+3)
...     import pdb; pdb.set_trace()
>>> f(3)
9
"""

```

Then an interactive Python session may look like this:

```python
>>> import a, doctest
>>> doctest.testmod(a)
--Return--
> <doctest a[1]>(3)g()->None
-> import pdb; pdb.set_trace()
(Pdb) list
  1     def g(x):
  2         print(x+3)
  3  ->     import pdb; pdb.set_trace()
[EOF]
(Pdb) p x
6
(Pdb) step
--Return--
> <doctest a[0]>(2)f()->None
-> g(x*2)
(Pdb) list
  1     def f(x):
  2  ->     g(x*2)
[EOF]
(Pdb) p x
3
(Pdb) step
--Return--
> <doctest a[2]>(1)?()->None
-> f(3)
(Pdb) cont
(0, 3)
>>>

```

Functions that translate doctests into Python code and may then execute the produced code beneath the debugger:

[Subject index](INDEX.md) · [Previous](doctest-output-comparison-and-differences.md) · [Continue](doctest-script-from-examples-to-doctest-debug-src.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

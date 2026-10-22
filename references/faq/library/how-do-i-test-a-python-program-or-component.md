# How do I test a Python program or component?

### Common tasks

### How do I test a Python program or component?

There are two testing frameworks bundled with Python. The [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module locates examples within a module's docstrings, executes them, and checks the produced output against the expected output recorded in the docstring.

A more elaborate testing framework, the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module, is patterned after the Java and Smalltalk testing frameworks.

Testing becomes simpler when your program follows sound modular design. Aim to wrap nearly all functionality inside functions or class methods ? which now and then yields the pleasant surprise of a faster program (since reading local variables outpaces reading globals). The program should also steer clear of relying on mutating global variables, because that complicates testing considerably.

Your program's ?global main logic? might be nothing more than

```python
if __name__ == "__main__":
    main_logic()

```

placed at the foot of your program's main module.

After your program has been arranged into a manageable set of function and class behaviours, write test functions that put those behaviours through their paces. Each module can carry an associated test suite that automates a series of tests. Though that may sound laborious, the brevity and flexibility of Python make it remarkably easy. Coding becomes far more enjoyable and entertaining when you write your test functions alongside the ?production code?, because that uncovers bugs and even design flaws sooner.

A ?support module? not meant to serve as a program's main module can carry its own self-test.

```python
if __name__ == "__main__":
    self_test()

```

Even programs that talk to intricate external interfaces can be tested while those interfaces are offline, by substituting ?fake? interfaces coded in Python.

[Subject index](INDEX.md)

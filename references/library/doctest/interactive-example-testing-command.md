# doctest`doctest` - Test interactive Python examples - Code example: $ python example.py

```shell
$ python example.py
$

```

Nothing was printed! That is expected behavior, and it signals that every example checked out. Hand the script a `-v` flag and `doctest` will emit a thorough log of each attempt, capped by a summary at the close:

```shell
$ python example.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok

```

Continuing in that fashion, it finally wraps up with:

```none
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
2 items passed all tests:
   1 test in __main__
   6 tests in __main__.factorial
7 tests in 2 items.
7 passed.
Test passed.
$

```

With that, you have enough grounding to begin putting `doctest` to good use! Dive right in. Fuller detail follows in the sections below. Keep in mind that the standard Python test suite and its libraries are full of doctest examples. A particularly instructive collection lives in the standard test file `Lib/test/test_doctest/test_doctest.py`.

Added in version 3.13: Coloring is applied to the output automatically, and you may steer it [controlled using environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color).

[Subject index](INDEX.md) · [Previous](interactive-example-testing-overview.md) · [Continue](simple-usage-checking-examples-in-docstrings.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

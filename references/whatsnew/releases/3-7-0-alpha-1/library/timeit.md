# Python 3.7.0 alpha 1 / library / timeit

[bpo-28469](https://bugs.python.org/issue?@action=redirect&bpo=28469): For autoranging, timeit now walks the sequence 1, 2, 5, 10, 20, 50,… in place of 1, 10, 100,…

[bpo-28240](https://bugs.python.org/issue?@action=redirect&bpo=28240): timeit: dropped the `-c/--clock` plus `-t/--time` command line options, which had been deprecated since Python 3.3.

[bpo-28240](https://bugs.python.org/issue?@action=redirect&bpo=28240): For greater reliability, timeit now runs each benchmark 5 times rather than only 3.

[bpo-28240](https://bugs.python.org/issue?@action=redirect&bpo=28240): timeit autorange now performs a single loop iteration whenever a benchmark finishes in under 10 seconds, rather than the previous 10 iterations. “python3 -m timeit -s ‘import time’ ‘time.sleep(1)’” now needs 4 seconds in place of 40 seconds.

- Distutils.sdist now searches for README and setup.py files using case sensitivity. That behavior lines up with what Setuptools 6.0 and newer do. Consult [setuptools 100](https://github.com/pypa/setuptools/issues/100) for the reasoning.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

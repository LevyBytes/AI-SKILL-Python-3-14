# Python 3.7.0 alpha 1 / tools demos / python

[bpo-30983](https://bugs.python.org/issue?@action=redirect&bpo=30983): The gdb integration commands (py-bt, and the rest) once again function on optimized shared builds. [**PEP 523**](https://peps.python.org/pep-0523/) brought in _PyEval_EvalFrameDefault, which folds PyEval_EvalFrameEx into itself on non-debug shared builds. That regression disabled py-bt, py-up, plus several other Python-aware gdb helpers. A fix arrived by restricting python-gdb.py to scan solely for _PyEval_EvalFrameDefault frames. The first patch came from Bruno ?Polaco? Penteado.

[bpo-29367](https://bugs.python.org/issue?@action=redirect&bpo=29367): Support for `method-wrapper` (`wrapperobject`) objects was added to python-gdb.py.

[bpo-28023](https://bugs.python.org/issue?@action=redirect&bpo=28023): Corrected python-gdb.py, which had lacked support for the new dict implementation.

[bpo-15369](https://bugs.python.org/issue?@action=redirect&bpo=15369): The pybench together with the pystone microbenchmark were dropped from Tools. Switch instead to the fresh Python benchmark suite at [https://github.com/python/pyperformance](https://github.com/python/pyperformance), which proves more dependable and ships a portable pybench that runs under both Python 2 and Python 3.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

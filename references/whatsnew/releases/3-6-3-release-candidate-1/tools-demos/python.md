# Python 3.6.3 release candidate 1 / tools demos / python

[bpo-30983](https://bugs.python.org/issue?@action=redirect&bpo=30983): The gdb integration commands (py-bt, and so on) now function on optimized shared builds as well. [**PEP 523**](https://peps.python.org/pep-0523/) brought in _PyEval_EvalFrameDefault, which inlines PyEval_EvalFrameEx within non-debug shared builds. That had wrecked the use of py-bt, py-up, plus a handful of other Python-oriented gdb integrations. The fix is to search exclusively for _PyEval_EvalFrameDefault frames inside python-gdb.py. Bruno "Polaco" Penteado supplied the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

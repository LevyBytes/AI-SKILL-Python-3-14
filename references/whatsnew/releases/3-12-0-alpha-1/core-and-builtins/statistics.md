# Python 3.12.0 alpha 1 / core and builtins / statistics

[gh-97670](https://github.com/python/cpython/issues/97670): The `sys.getdxp()` function and the `Tools/scripts/analyze_dxp.py` script are now gone. DXP is short for "dynamic execution pairs". They tied into the `DYNAMIC_EXECUTION_PROFILE` and `DXPAIRS` macros, both removed back in Python 3.11. Python can instead be built using [`./configure --enable-pystats`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-pystats) to collect statistics about Python opcodes. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

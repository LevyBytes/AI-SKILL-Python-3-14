# Python 3.10.0 beta 1 / c api / veryhigh

[bpo-43868](https://bugs.python.org/issue?@action=redirect&bpo=43868): On Windows, [`PyOS_ReadlineFunctionPointer()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer) is no longer exported by the limited C API headers or by `python3.dll`. As with any function accepting `FILE*`, it falls outside the stable ABI.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

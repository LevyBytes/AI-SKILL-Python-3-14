# Python 3.11.0 alpha 1 / core and builtins / typeobj

[bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908): Heap types carrying the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) flag are now able to inherit the [**PEP 590**](https://peps.python.org/pep-0590/) vectorcall protocol. Up to now that ability belonged only to [static types](https://docs.python.org/3.14/c-api/typeobj.html#static-types). Erlend E. Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

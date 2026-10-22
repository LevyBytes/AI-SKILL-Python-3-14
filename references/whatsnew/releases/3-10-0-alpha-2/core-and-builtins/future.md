# Python 3.10.0 alpha 2 / core and builtins / future

[bpo-38605](https://bugs.python.org/issue?@action=redirect&bpo=38605): Switch on `from __future__ import annotations` ([**PEP 563**](https://peps.python.org/pep-0563/)) as the default. Values residing in [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) dicts are strings these days ? `{"x": "int"}` in place of `{"x": int}`, for instance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

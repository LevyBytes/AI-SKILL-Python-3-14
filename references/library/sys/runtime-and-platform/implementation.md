# sys.implementation

sys.implementation

An object that holds information describing the implementation of the Python interpreter now running. Every Python implementation is required to provide the following attributes.

*name* is the implementation's identifier, e.g. `'cpython'`. The Python implementation itself fixes the actual string, but it is guaranteed to be lower case.

*version* is a named tuple sharing the format of `sys.version_info`. It stands for the version of the Python *implementation*. That is a separate notion from the particular version of the Python *language* that the running interpreter conforms to, which `sys.version_info` captures. For instance, on PyPy 1.8 the value of `sys.implementation.version` might be `sys.version_info(1, 8, 0, 'final', 0)`, while `sys.version_info` would read `sys.version_info(2, 7, 2, 'final', 0)`. On CPython the two coincide, since CPython is the reference implementation.

*hexversion* is the implementation version in hexadecimal format, like `sys.hexversion`.

*cache_tag* is the tag the import machinery applies within the filenames of cached modules. As a rule it combines the implementation's name and version, such as `'cpython-33'`. A Python implementation may, however, substitute some other value when that suits. Setting `cache_tag` to `None` signals that module caching ought to be turned off.

*supports_isolated_interpreters* is a boolean reporting whether the implementation can run several isolated interpreters. On most platforms CPython sets it to `True`. Any platform offering that capability provides the low-level `_interpreters` module.

See also

[**PEP 684**](https://peps.python.org/pep-0684/), [**PEP 734**](https://peps.python.org/pep-0734/), and [`concurrent.interpreters`](https://docs.python.org/3.14/library/concurrent.interpreters.html#module-concurrent.interpreters).

`sys.implementation` may carry extra attributes that are particular to the Python implementation. Such non-standard attributes have to begin with an underscore, and they are not covered here. Whatever it holds, `sys.implementation` stays fixed across a single run of the interpreter, and across implementation versions as well. (Across Python language versions it can change, however.) Consult [**PEP 421**](https://peps.python.org/pep-0421/) for further information.

Added in version 3.3.

Changed in version 3.14: Added `supports_isolated_interpreters` field.

Note

Any new required attribute may only be introduced by way of the usual PEP process. See [**PEP 421**](https://peps.python.org/pep-0421/) for more information.

[API family](INDEX.md) · [sys context index](../INDEX.md).

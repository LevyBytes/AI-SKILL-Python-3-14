# Python 3.7.0 alpha 1 / library / ctypes

[bpo-18893](https://bugs.python.org/issue?@action=redirect&bpo=18893): Repaired faulty exception handling within Lib/ctypes/macholib/dyld.py. Madison May provided the patch.

[bpo-25659](https://bugs.python.org/issue?@action=redirect&bpo=25659): Within ctypes, a crash is now avoided when from_buffer() or from_buffer_copy() get invoked on abstract classes such as Array.

[bpo-10746](https://bugs.python.org/issue?@action=redirect&bpo=10746): Repair ctypes emitting the wrong [**PEP 3118**](https://peps.python.org/pep-3118/) type codes for integer types.

[bpo-30470](https://bugs.python.org/issue?@action=redirect&bpo=30470): Invalid ctypes call protection under Windows is now deprecated. Mariatta Wijaya provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

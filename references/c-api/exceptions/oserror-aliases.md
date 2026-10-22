# OSError aliases

### OSError aliases

The entries below serve as compatibility aliases pointing at `PyExc_OSError`.

Changed in version 3.3: Before this release, each of these aliases was its own distinct exception type.

| C name | Python name | Notes |
| --- | --- | --- |
| PyObject *PyExc_EnvironmentError * Part of the Stable ABI.* | `OSError` |  |
| PyObject *PyExc_IOError * Part of the Stable ABI.* | `OSError` |  |
| PyObject *PyExc_WindowsError * Part of the Stable ABI on Windows since version 3.7.* | `OSError` | [win] |

Notes:

   [win]

`PyExc_WindowsError` exists solely on the Windows platform; guard any code referencing it by checking whether the preprocessor macro `MS_WINDOWS` has been defined.

[Subject index](INDEX.md) · [Previous source contract](exception-types.md) · [Following source contract](warning-types.md)

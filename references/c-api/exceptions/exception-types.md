# Exception types

### Exception types

| C name | Python name |
| --- | --- |
| PyObject *PyExc_BaseException * Part of the Stable ABI.* | `BaseException` |
| PyObject *PyExc_BaseExceptionGroup * Part of the Stable ABI since version 3.11.* | `BaseExceptionGroup` |
| PyObject *PyExc_Exception * Part of the Stable ABI.* | `Exception` |
| PyObject *PyExc_ArithmeticError * Part of the Stable ABI.* | `ArithmeticError` |
| PyObject *PyExc_AssertionError * Part of the Stable ABI.* | `AssertionError` |
| PyObject *PyExc_AttributeError * Part of the Stable ABI.* | `AttributeError` |
| PyObject *PyExc_BlockingIOError * Part of the Stable ABI since version 3.7.* | `BlockingIOError` |
| PyObject *PyExc_BrokenPipeError * Part of the Stable ABI since version 3.7.* | `BrokenPipeError` |
| PyObject *PyExc_BufferError * Part of the Stable ABI.* | `BufferError` |
| PyObject *PyExc_ChildProcessError * Part of the Stable ABI since version 3.7.* | `ChildProcessError` |
| PyObject *PyExc_ConnectionAbortedError * Part of the Stable ABI since version 3.7.* | `ConnectionAbortedError` |
| PyObject *PyExc_ConnectionError * Part of the Stable ABI since version 3.7.* | `ConnectionError` |
| PyObject *PyExc_ConnectionRefusedError * Part of the Stable ABI since version 3.7.* | `ConnectionRefusedError` |
| PyObject *PyExc_ConnectionResetError * Part of the Stable ABI since version 3.7.* | `ConnectionResetError` |
| PyObject *PyExc_EOFError * Part of the Stable ABI.* | `EOFError` |
| PyObject *PyExc_FileExistsError * Part of the Stable ABI since version 3.7.* | `FileExistsError` |
| PyObject *PyExc_FileNotFoundError * Part of the Stable ABI since version 3.7.* | `FileNotFoundError` |
| PyObject *PyExc_FloatingPointError * Part of the Stable ABI.* | `FloatingPointError` |
| PyObject *PyExc_GeneratorExit * Part of the Stable ABI.* | `GeneratorExit` |
| PyObject *PyExc_ImportError * Part of the Stable ABI.* | `ImportError` |
| PyObject *PyExc_IndentationError * Part of the Stable ABI.* | `IndentationError` |
| PyObject *PyExc_IndexError * Part of the Stable ABI.* | `IndexError` |
| PyObject *PyExc_InterruptedError * Part of the Stable ABI since version 3.7.* | `InterruptedError` |
| PyObject *PyExc_IsADirectoryError * Part of the Stable ABI since version 3.7.* | `IsADirectoryError` |
| PyObject *PyExc_KeyError * Part of the Stable ABI.* | `KeyError` |
| PyObject *PyExc_KeyboardInterrupt * Part of the Stable ABI.* | `KeyboardInterrupt` |
| PyObject *PyExc_LookupError * Part of the Stable ABI.* | `LookupError` |
| PyObject *PyExc_MemoryError * Part of the Stable ABI.* | `MemoryError` |
| PyObject *PyExc_ModuleNotFoundError * Part of the Stable ABI since version 3.6.* | `ModuleNotFoundError` |
| PyObject *PyExc_NameError * Part of the Stable ABI.* | `NameError` |
| PyObject *PyExc_NotADirectoryError * Part of the Stable ABI since version 3.7.* | `NotADirectoryError` |
| PyObject *PyExc_NotImplementedError * Part of the Stable ABI.* | `NotImplementedError` |
| PyObject *PyExc_OSError * Part of the Stable ABI.* | `OSError` |
| PyObject *PyExc_OverflowError * Part of the Stable ABI.* | `OverflowError` |
| PyObject *PyExc_PermissionError * Part of the Stable ABI since version 3.7.* | `PermissionError` |
| PyObject *PyExc_ProcessLookupError * Part of the Stable ABI since version 3.7.* | `ProcessLookupError` |
| PyObject *PyExc_PythonFinalizationError | `PythonFinalizationError` |
| PyObject *PyExc_RecursionError * Part of the Stable ABI since version 3.7.* | `RecursionError` |
| PyObject *PyExc_ReferenceError * Part of the Stable ABI.* | `ReferenceError` |
| PyObject *PyExc_RuntimeError * Part of the Stable ABI.* | `RuntimeError` |
| PyObject *PyExc_StopAsyncIteration * Part of the Stable ABI since version 3.7.* | `StopAsyncIteration` |
| PyObject *PyExc_StopIteration * Part of the Stable ABI.* | `StopIteration` |
| PyObject *PyExc_SyntaxError * Part of the Stable ABI.* | `SyntaxError` |
| PyObject *PyExc_SystemError * Part of the Stable ABI.* | `SystemError` |
| PyObject *PyExc_SystemExit * Part of the Stable ABI.* | `SystemExit` |
| PyObject *PyExc_TabError * Part of the Stable ABI.* | `TabError` |
| PyObject *PyExc_TimeoutError * Part of the Stable ABI since version 3.7.* | `TimeoutError` |
| PyObject *PyExc_TypeError * Part of the Stable ABI.* | `TypeError` |
| PyObject *PyExc_UnboundLocalError * Part of the Stable ABI.* | `UnboundLocalError` |
| PyObject *PyExc_UnicodeDecodeError * Part of the Stable ABI.* | `UnicodeDecodeError` |
| PyObject *PyExc_UnicodeEncodeError * Part of the Stable ABI.* | `UnicodeEncodeError` |
| PyObject *PyExc_UnicodeError * Part of the Stable ABI.* | `UnicodeError` |
| PyObject *PyExc_UnicodeTranslateError * Part of the Stable ABI.* | `UnicodeTranslateError` |
| PyObject *PyExc_ValueError * Part of the Stable ABI.* | `ValueError` |
| PyObject *PyExc_ZeroDivisionError * Part of the Stable ABI.* | `ZeroDivisionError` |

Added in version 3.3: `PyExc_BlockingIOError`, `PyExc_BrokenPipeError`, `PyExc_ChildProcessError`, `PyExc_ConnectionError`, `PyExc_ConnectionAbortedError`, `PyExc_ConnectionRefusedError`, `PyExc_ConnectionResetError`, `PyExc_FileExistsError`, `PyExc_FileNotFoundError`, `PyExc_InterruptedError`, `PyExc_IsADirectoryError`, `PyExc_NotADirectoryError`, `PyExc_PermissionError`, `PyExc_ProcessLookupError` and `PyExc_TimeoutError` were introduced following [**PEP 3151**](https://peps.python.org/pep-3151/).

Added in version 3.5: `PyExc_StopAsyncIteration` and `PyExc_RecursionError`.

Added in version 3.6: `PyExc_ModuleNotFoundError`.

Added in version 3.11: `PyExc_BaseExceptionGroup`.

[Subject index](INDEX.md) · [Previous source contract](exception-and-warning-types.md) · [Following source contract](oserror-aliases.md)

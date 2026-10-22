# Initializing and finalizing the interpreter

### Initializing and finalizing the interpreter

 void Py_Initialize()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Bring the Python interpreter online. Within an application embedding Python, invoke this ahead of any other Python/C API call; the handful of exceptions appear under Before Python Initialization.

Doing so populates the table of loaded modules (`sys.modules`) and builds the core modules [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins), [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) and [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys). The module search path (`sys.path`) is set up as well. `sys.argv` is left unset; rely on the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) API to populate it. A second invocation (without an intervening `Py_FinalizeEx()`) has no effect. The function returns nothing; a failed initialization is a fatal error.

To tailor the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config), turn to `Py_InitializeFromConfig()`.

Note

On Windows, switches the console mode from `O_TEXT` to `O_BINARY`, an effect that extends to non-Python code using the console through the C Runtime.

 void Py_InitializeEx(int initsigs)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `Py_Initialize()` when *initsigs* equals `1`. When *initsigs* equals `0`, it bypasses the registration of signal handlers, which can be handy when CPython is embedded within a bigger application.

To tailor the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config), turn to `Py_InitializeFromConfig()`.

 [PyStatus](https://docs.python.org/3.14/c-api/init_config.html#c.PyStatus) Py_InitializeFromConfig(const [PyConfig](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) *config)

Start Python up from the *config* configuration, following [Initialization with PyConfig](https://docs.python.org/3.14/c-api/init_config.html#init-from-config).

Turn to the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) section for how to pre-initialize the interpreter, fill in the runtime configuration structure, and inspect the status structure that comes back.

 int Py_IsInitialized()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield true (nonzero) once the Python interpreter is initialized, and false (zero) otherwise. Following a `Py_FinalizeEx()` call, the result stays false until `Py_Initialize()` runs once more.

 int Py_IsFinalizing()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Yield true (non-zero) while the primary Python interpreter is [shutting down](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown). Otherwise yield false (zero).

Added in version 3.13.

 int Py_FinalizeEx()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.6.*

Reverse every initialization performed by `Py_Initialize()` and the later use of Python/C API functions, and tear down all sub-interpreters (see [`Py_NewInterpreter()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_NewInterpreter) below) that were created since the most recent `Py_Initialize()` call and not yet destroyed. A second invocation (without first calling `Py_Initialize()` again) has no effect.

Because this mirrors `Py_Initialize()`, run it on the same thread with the same interpreter active, namely the main thread and the main interpreter. Never call it during a `Py_RunMain()` run.

The usual return value is `0`. Should anything go wrong while finalizing (for instance flushing buffered data), `-1` comes back.

Keep in mind that Python makes a best effort to release every byte the interpreter allocated. Accordingly, any C-Extension ought to dispose of all the PyObjects it allocated earlier before they get reused across later `Py_Initialize()` calls. Failing to do so risks vulnerabilities and faulty behavior.

There are several motivations for offering this function. An embedding application may wish to restart Python without restarting the whole application. An application that pulled in the Python interpreter from a dynamically loadable library (or DLL) may wish to release every byte Python allocated prior to unloading that DLL. While chasing memory leaks, a developer may wish to release all of Python's allocations before quitting the application.

**Bugs and caveats:** Modules and the objects within them are torn down in an arbitrary order; consequently destructors ([`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) methods) may break when they rely on other objects (even functions) or modules. Extension modules that Python loaded dynamically remain loaded. Modest amounts of memory the Python interpreter allocated might linger unfreed (please report any leak you discover). Memory held in circular references among objects is not reclaimed. Interned strings are all freed no matter their reference count. Certain memory that extension modules allocated may stay unfreed. Some extensions may misbehave if their initialization routine runs more than once; that scenario arises if an application calls `Py_Initialize()` and `Py_FinalizeEx()` repeatedly. `Py_FinalizeEx()` must never recurse into itself. Hence no code that could execute as part of the interpreter shutdown sequence may call it, including [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) handlers, object finalizers, or any code that might run while the stdout and stderr files are being flushed.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython._PySys_ClearAuditHooks` with no arguments.

Added in version 3.6.

 void Py_Finalize()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A backwards-compatible variant of `Py_FinalizeEx()` that ignores the return value.

 int Py_BytesMain(int argc, char **argv)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

Resembles `Py_Main()`, except *argv* is an array of bytes strings, which lets the calling application hand off the text-decoding step to the CPython runtime.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous source contract](py-unbufferedstdioflag-to-py-verboseflag.md) · [Following source contract](py-main.md)

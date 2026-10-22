# Threads and interpreter lock

Open when checking Python definitions for threads and interpreter lock.

## thread state

The data the CPython runtime relies on to run within an OS thread. As an example, this takes in the current exception, should there be one, together with the state of the bytecode interpreter.

Each thread state is tied to one single OS thread, though threads may have a number of thread states on hand. No more than one of them can be attached at any moment.

To call most of Python's C API you need an attached thread state, save where a function explicitly states otherwise. The bytecode interpreter runs solely under an attached thread state.

Each thread state belongs to one single interpreter, yet each interpreter may hold many thread states, including several for the same OS thread. Thread states from different interpreters may be tied to one thread, but only one can be attached within that thread at any one time.

See [Thread State and the Global Interpreter Lock](https://docs.python.org/3.14/c-api/threads.html#threads) for more information.

## attached thread state

A thread state that is currently live for the present OS thread.

While a thread state is attached, the OS thread reaches the entire Python C API and may safely drive the bytecode interpreter.

Barring an explicit note to the contrary in a given function, trying to call into the C API without an attached thread state yields either a fatal error or undefined behavior. The user may attach and detach a thread state deliberately through the C API, or the runtime may do so on its own, which includes during blocking C calls and via the bytecode interpreter between successive calls.

Across the majority of Python builds, holding an attached thread state means the caller owns the GIL for the active interpreter, so at any single instant only one OS thread can hold an attached thread state. In free-threaded builds of Python, several threads may hold an attached thread state at once, which enables genuine parallelism of the bytecode interpreter.

## global interpreter lock

The device the CPython interpreter relies on to ensure that no more than one thread runs Python bytecode at any time. It eases the CPython implementation by rendering the object model (which includes essential built-in types like [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)) implicitly protected against concurrent access. Putting a lock around the whole interpreter simplifies making the interpreter multi-threaded, though it sacrifices a good deal of the parallelism that multi-processor hardware offers.

That said, certain extension modules, whether bundled or external, are written to release the GIL while performing computation-heavy work like compression or hashing. The GIL is likewise always released during I/O.

Beginning with Python 3.13, the [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) build configuration lets you turn off the GIL. A free-threaded build normally runs with the GIL disabled. The [`-X gil`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option or [`PYTHON_GIL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_GIL) environment variable can control its runtime state; importing an extension that does not declare free-threading support can enable it automatically. See the [free-threading runtime guidance](https://docs.python.org/3.14/howto/free-threading-python.html#the-global-interpreter-lock-in-free-threaded-python). This capability brings better performance to multi-threaded programs and makes efficient use of multi-core CPUs more straightforward. For additional detail, see [**PEP 703**](https://peps.python.org/pep-0703/).

In earlier releases of Python's C API, a function could state that the GIL had to be held for it to be usable. That amounts to holding an attached thread state.

## GIL

See global interpreter lock.

## free-threaded build

A CPython build offering free threading support, set up via the [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) option prior to compilation.

See [Python support for free threading](https://docs.python.org/3.14/howto/free-threading-python.html#freethreading-python-howto).

## free threading

A threading scheme permitting several threads to execute Python bytecode at once inside a single interpreter. This differs from the global interpreter lock, under which just one thread runs Python bytecode at any moment. See [**PEP 703**](https://peps.python.org/pep-0703/).

[Glossary context index](INDEX.md).

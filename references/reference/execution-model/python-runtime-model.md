# 4.4.2. Python Runtime Model

### 4.4.2. Python Runtime Model

Those same conceptual layers hold for every Python program, with a few data layers peculiar to Python layered on:

>   **host machine**  **process** (global resources)  Python global runtime (*state*)  Python interpreter (*state*)  **thread** (runs Python bytecode and “C-API”)  Python thread *state*

At the conceptual level, the launch of a Python program looks precisely like that diagram, one of each. The runtime may expand to hold several interpreters, and each interpreter may expand to hold several thread states.

Note

A Python implementation need not realize the runtime layers as distinct or even as concrete things. The sole exception is wherever distinct layers are spelled out or surfaced to users directly, as through the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module.

Note

By convention the first interpreter is the "main" interpreter. Certain Python implementations, CPython among them, hand special roles to the main interpreter.

In the same vein, the host thread on which the runtime got initialized is called the "main" thread. It need not be the process' initial thread, though the two often coincide. In some cases "main thread" carries an even narrower meaning, denoting the initial thread state. A Python runtime might hand specific duties — signal handling, for one — to the main thread.

Taken altogether, the Python runtime is made up of the global runtime state, the interpreters, and the thread states. The runtime keeps all that state consistent across its lifetime, especially when several host threads are in play.

The global runtime, conceptually speaking, is nothing more than a set of interpreters. Those interpreters, while otherwise isolated and independent from one another, may share certain data or other resources. Keeping these global resources safe falls to the runtime. How those resources actually behave and get managed is implementation-specific. In the end, the global runtime's outward usefulness comes down to managing interpreters.

By contrast, an "interpreter" is conceptually the thing we would ordinarily picture as the (full-featured) "Python runtime". When machine code running on a host thread interacts with the Python runtime, the call into Python happens in the context of one particular interpreter.

Note

The "interpreter" meant here is not the same thing as the "bytecode interpreter" — the latter being what runs routinely in threads, executing compiled Python code.

Ideally, "Python runtime" would name what we now call the "interpreter". Yet "interpreter" has been its name ever since it was introduced back in 1997 ([CPython:a027efa5b](https://github.com/python/cpython/commit/a027efa5b)).

Each interpreter wholly wraps up every bit of the non-process-global, non-thread-specific state the Python runtime needs in order to function. Tellingly, an interpreter's state carries over between uses. Among what it holds is core data such as [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules). The runtime sees to it that several threads using one interpreter share it between them safely.

A Python implementation may permit several interpreters to be in use at the same time within one process. Each is independent and isolated from the rest. Every interpreter, for instance, has its own [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

When it comes to thread-specific runtime state, every interpreter holds a set of thread states that it manages — much as the global runtime holds a set of interpreters. It can carry as many thread states as it needs host threads. It may even carry several thread states for one host thread, though that arrangement is less common.

In conceptual terms, every thread state carries whatever per-thread runtime information an interpreter requires in order to run within a single host thread. Among the things a thread state holds are the exception currently being raised together with that thread’s Python call stack. Beyond those, it can carry additional resources specific to the thread.

Note

On occasion the phrase “Python thread” gets used to mean a thread state, yet most of the time it denotes a thread spun up through the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module.

Throughout however long it exists, any given thread state stays bound to precisely one interpreter and precisely one host thread. Its use never extends past that single thread paired with that single interpreter.

It is possible for several thread states to be bound to one and the same host thread, be that across distinct interpreters or within a single interpreter. That said, on any one host thread, the thread is limited to using just a single one of its associated thread states at any moment.

Each thread state remains separate and self-contained relative to the others, holding no data in common — the lone exception being that they might share an interpreter along with objects or other resources owned by that interpreter.

After a program has started executing, you can spawn fresh Python threads via the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module (wherever the platform and the Python implementation provide thread support). To launch extra processes, turn to the [`os`](https://docs.python.org/3.14/library/os.html#module-os), [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess), and [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) modules. For making and working with interpreters, there is the [`interpreters`](https://docs.python.org/3.14/library/concurrent.interpreters.html#module-concurrent.interpreters) module. Within each interpreter, coroutines (async) may be driven through [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio), as a rule confined to one thread alone (frequently the main one).

Footnotes

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Owning language section](general-computing-model.md) · [Previous source section](general-computing-model.md)

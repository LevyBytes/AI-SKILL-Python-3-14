# Detaching the thread state from extension code

### Detaching the thread state from extension code

The majority of extension code that touches the [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) follows this straightforward shape:

```c
Save the thread state in a local variable.
... Do some blocking I/O operation ...
Restore the thread state from the local variable.

```

Because the pattern recurs so frequently, two macros are provided to streamline it:

```c
Py_BEGIN_ALLOW_THREADS
... Do some blocking I/O operation ...
Py_END_ALLOW_THREADS

```

`Py_BEGIN_ALLOW_THREADS` starts a fresh block and introduces a concealed local variable; `Py_END_ALLOW_THREADS` ends that block.

What the block above expands into is the following code:

```c
PyThreadState *_save;

_save = PyEval_SaveThread();
... Do some blocking I/O operation ...
PyEval_RestoreThread(_save);

```

Here's the mechanism behind these functions:

Having an attached thread state means the GIL is held on behalf of the interpreter. You detach it by calling `PyEval_SaveThread()` and keeping the returned value in a local variable.

Detaching the thread state releases the GIL, letting other threads attach to the interpreter and run while the present thread is busy with blocking I/O. Once the I/O finishes, you reattach the former thread state by invoking `PyEval_RestoreThread()`, which blocks until it can acquire the GIL.

Note

Although blocking I/O is the typical reason to detach the thread state, doing so is also worthwhile around drawn-out native code that requires neither Python objects nor Python's C API. As an illustration, the standard [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) and [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) modules detach the [thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) while they compress or hash data.

On a [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) typically isn't a factor, yet **detaching the thread state is still required**, since the interpreter must occasionally halt every thread to obtain a coherent picture of Python objects free from race-condition hazards. As one example, CPython at present pauses all threads briefly while the garbage collector runs.

Warning

Detaching the thread state may produce surprising behavior while the interpreter is being finalized. Consult [Cautions regarding runtime finalization](https://docs.python.org/3.14/c-api/interp-lifecycle.html#cautions-regarding-runtime-finalization) for additional detail.

[Subject index](INDEX.md) · [Previous source contract](thread-states-and-the-global-interpreter-lock.md) · [Following source contract](py-begin-allow-threads-to-py-unblock-threads.md)

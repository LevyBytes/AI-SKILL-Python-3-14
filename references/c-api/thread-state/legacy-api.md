# Legacy API

### Legacy API

A second widespread approach for running Python code from a non-Python thread employs `PyGILState_Ensure()` and then a `PyGILState_Release()` call.

These functions fare poorly once several interpreters coexist within the Python process. When no Python interpreter has yet been touched on the current thread (a typical situation for threads spun up outside Python), `PyGILState_Ensure` builds and attaches a thread state for the "main" interpreter (which is the first interpreter in the Python process).

On top of that, these functions carry thread-safety problems while the interpreter is finalizing. Calling `PyGILState_Ensure` during finalization is likely to crash the process.

These functions are used like so:

```c
PyGILState_STATE gstate;
gstate = PyGILState_Ensure();

/* Perform Python actions here. */
result = CallSomeFunction();
/* evaluate result or handle exception */

/* Release the thread. No Python API allowed beyond this point. */
PyGILState_Release(gstate);

```

[Subject index](INDEX.md) · [Previous source contract](non-python-created-threads.md) · [Following source contract](cautions-about-fork.md)

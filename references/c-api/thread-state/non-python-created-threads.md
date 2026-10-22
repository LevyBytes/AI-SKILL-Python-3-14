# Non-Python created threads

### Non-Python created threads

Threads spawned via the purpose-built Python APIs (the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module being one) get a thread state linked to them automatically. By contrast, a thread originating in native code — for instance, from a third-party library that runs its own thread management — carries no attached thread state.

Whenever you must run Python code from such threads (frequently as part of a callback API exposed by the third-party library mentioned above), you have to first enroll those threads with the interpreter by building a fresh thread state and attaching it.

The sturdiest approach is `PyThreadState_New()` followed by `PyThreadState_Swap()`.

Note

`PyThreadState_New` takes an argument that points to the interpreter you want; you can obtain such a pointer by calling [`PyInterpreterState_Get()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_Get) from wherever the thread was created.

For example:

```c
/* The return value of PyInterpreterState_Get() from the
   function that created this thread. */
PyInterpreterState *interp = thread_data->interp;

/* Create a new thread state for the interpreter. It does not start out
   attached. */
PyThreadState *tstate = PyThreadState_New(interp);

/* Attach the thread state, which will acquire the GIL. */
PyThreadState_Swap(tstate);

/* Perform Python actions here. */
result = CallSomeFunction();
/* evaluate result or handle exception */

/* Destroy the thread state. No Python API allowed beyond this point. */
PyThreadState_Clear(tstate);
PyThreadState_DeleteCurrent();

```

Warning

Should the interpreter have been finalized before `PyThreadState_Swap` ran, `interp` is left as a dangling pointer!

[Subject index](INDEX.md) · [Previous source contract](py-begin-allow-threads-to-py-unblock-threads.md) · [Following source contract](legacy-api.md)

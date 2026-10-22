# threading: `threading.Thread`

### Thread objects

An activity carried out within a distinct thread of control is what the `Thread` class stands for. You can name that activity in either of two ways: hand a callable to the constructor, or override the `run()` method inside a subclass. Apart from the constructor, no further methods ought to be overridden in a subclass. Put differently, override *only* this class’s `__init__()` and `run()` methods.

After a thread object exists, you launch its activity by calling the thread’s `start()` method. Doing so runs the `run()` method within its own thread of control.

From the moment its activity begins, a thread counts as ‘alive’. That status ends once its `run()` method finishes — whether it completes normally or throws an exception that goes uncaught. Whether a thread is alive can be checked with the `is_alive()` method.

Any other thread is free to invoke a thread’s `join()` method. That holds the calling thread back until the thread on which `join()` was called has ended.

Every thread carries a name. You can hand that name to the constructor and then read or modify it via the `name` attribute.

When the `run()` method throws an exception, `threading.excepthook()` steps in to handle it. Out of the box, `threading.excepthook()` quietly disregards [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit).

Any thread may be marked as a “daemon thread”. What this flag means is that once nothing but daemon threads remain, the whole Python program shuts down. Its starting value is taken from the thread doing the creating. You set the flag either through the `daemon` property or via the *daemon* constructor argument.

Note

When shutdown happens, daemon threads are halted on the spot. Whatever resources they hold — open files, database transactions, and the like — might not be cleaned up correctly. Should you want your threads to wind down cleanly, keep them non-daemonic and rely on an appropriate signalling mechanism like an `Event`.

A “main thread” object exists; it stands for the program’s original thread of control in Python. It is not a daemon thread.

It is also possible for “dummy thread objects” to come into being. Such thread objects map to “alien threads” — threads of control begun beyond the threading module, for instance straight from C code. The functionality of dummy thread objects is limited; they always count as alive and daemonic, and they cannot be joined. Because there is no way to notice when alien threads finish, they are never removed.

 *class *threading.Thread(*group=None*, *target=None*, *name=None*, *args=()*, *kwargs={}*, ***, *daemon=None*, *context=None*)

Always invoke this constructor using keyword arguments. The arguments are:

*group* has to be `None`, being held in reserve for a later extension once a `ThreadGroup` class arrives.

*target* names the callable object that the `run()` method will call. It defaults to `None`, meaning nothing gets called.

*name* gives the thread’s name. Absent an explicit value, a distinct name is assembled as “Thread-*N*” (here *N* denotes some small decimal number), or as “Thread-*N* (target)” when the *target* argument is supplied, with “target” standing for `target.__name__`.

*args* is a list or tuple supplying the arguments for invoking the target. It defaults to `()`.

*kwargs* is a dictionary supplying the keyword arguments for invoking the target. It defaults to `{}`.

When *daemon* is not `None`, it expressly decides whether the thread is daemonic. With `None` (the default) the daemonic property carries over from the current thread.

*context* names the [`Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) value applied when the thread starts. Its default of `None` signals that the [`sys.flags.thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag governs the behaviour. When that flag is true, a thread begins holding a copy of the context belonging to whoever called `start()`. When it is false, the thread begins with an empty context. To deliberately begin with an empty context, supply a fresh instance of [`Context()`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context). To deliberately begin with a copy of the present context, supply the value returned by [`copy_context()`](https://docs.python.org/3.14/library/contextvars.html#contextvars.copy_context). On free-threaded builds the flag defaults to true, and false everywhere else.

When a subclass overrides the constructor, it has to be sure the base class constructor (`Thread.__init__()`) runs before it touches the thread in any other way.

Changed in version 3.3: Added the *daemon* parameter.

Changed in version 3.10: When the *name* argument is left out, fall back to the *target* name.

Changed in version 3.14: Added the *context* parameter.

[Subject index](INDEX.md) · [Previous](threading-local-class.md) · [Continue](threading-thread-start-to-threading-thread-setname.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)

# atexit`atexit` - Exit handlers

## atexit - Exit handlers

### `atexit` - Exit handlers

---

Functions for registering and unregistering cleanup callbacks are what the `atexit` module provides. A function once registered fires automatically when the interpreter shuts down normally. `atexit` invokes them in the *reverse* of their registration order; register `A`, `B`, and `C`, and at interpreter shutdown they execute as `C`, `B`, `A`.

**Note:** Functions registered through this module go uncalled when a signal Python doesn't handle kills the program, when Python hits a fatal internal error, or when [`os._exit()`](https://docs.python.org/3.14/library/os.html#os._exit) is invoked.

**Note:** What happens if you register or unregister functions from inside a cleanup function is undefined.

Changed in version 3.7: Under C-API subinterpreters, a registered function stays confined to whichever interpreter performed the registration.

 `atexit.register(*func*, **args*, ***kwargs*)`

Sign *func* up as a function to run at termination. Whatever optional arguments you want forwarded to *func* have to be given as arguments to `register()`. Registering the very same function with the same arguments more than once is allowed.

On an orderly program exit — say, a call to [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) or the main module finishing — each registered function is invoked in last-in, first-out sequence. The reasoning is that lower-level modules usually get imported ahead of higher-level ones and therefore should be torn down afterward.

Should an exception surface while the exit handlers run, a traceback is shown (except when [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) is raised) and the exception details are stored. Once every exit handler has had its turn, the most recent exception raised is raised again.

Because this function hands back *func*, you can apply it as a decorator.

Warning

Spawning new threads or calling [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) from a registered function risks a race condition: the main Python runtime thread may be releasing thread states just as internal [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) routines or the freshly forked process attempt to use that state. The outcome can be crashes in place of an orderly shutdown.

Changed in version 3.12: Trying to spawn a thread or [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) a process from inside a registered function now raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 `atexit.unregister(*func*)`

Strike *func* from the roster of functions slated to run at interpreter shutdown. `unregister()` quietly does nothing when *func* was never registered to begin with. Where *func* sits in the registry more than once, each appearance of it on the `atexit` call stack is taken out. Internally, equality comparisons (`==`) drive the removal, so the function references involved needn't share the same identity.

See also

Module [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline)

A handy `atexit` example covering the reading and writing of [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) history files.

[Subject index](INDEX.md) · [Continue](atexit-example.md)

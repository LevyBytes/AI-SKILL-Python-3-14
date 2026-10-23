# decimal - Working with threads

### Working with threads

For each thread, the `getcontext()` function reaches a separate `Context` object. Because thread contexts are kept apart, threads can apply changes (for example, `getcontext().prec=10`) without disturbing other threads.

In the same way, the `setcontext()` function automatically attaches its target to the current thread.

Should `setcontext()` not have been called before `getcontext()`, then `getcontext()` will automatically build a new context for the current thread to use. Fresh context objects take their default values from the `decimal.DefaultContext` object.

The [`sys.flags.thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag governs the context of new threads. When the flag is false, new threads begin with an empty context, and `getcontext()` builds a new context object on being called and uses the default values taken from *DefaultContext*. When the flag is true, new threads begin with a copy of the context belonging to the caller of [`threading.Thread.start()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.start).

To manage the defaults so that every thread uses identical values throughout the application, alter the *DefaultContext* object directly. Do this *before* launching any threads so that no race condition arises among threads calling `getcontext()`. For example:

```python
# Set applicationwide defaults for all threads about to be launched
DefaultContext.prec = 12
DefaultContext.rounding = ROUND_DOWN
DefaultContext.traps = ExtendedContext.traps.copy()
DefaultContext.traps[InvalidOperation] = 1
setcontext(DefaultContext)

# Afterwards, the threads can be started
t1.start()
t2.start()
t3.start()
 . . .

```

[Subject index](INDEX.md) · [Previous](special-values.md) · [Continue](recipes-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)

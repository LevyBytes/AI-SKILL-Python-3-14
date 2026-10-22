# concurrent.interpreters — Concurrency and Parallelism

### Concurrency and Parallelism

As already mentioned, interpreters by themselves deliver no concurrency at all. All they are is the isolated execution context the runtime employs *in the current thread*. That isolation lends them a process-like flavor, yet they keep the in-process efficiency you get from threads.

Even so, interpreters lend themselves naturally to a few styles of concurrency. The isolation has a potent side effect: it opens a route to concurrency unlike what async or threads give you. The result resembles the CSP or actor model — a model that’s comparatively easy to reason through.

You can lean on that model within one thread, hopping back and forth between interpreters, Stackless-fashion. The model earns its keep more, though, once you pair interpreters with several threads. That largely amounts to launching a new thread, switching to a different interpreter there, and running whatever you like.

In Python every real thread — even if the main thread is all you’re using — owns its own *current* execution context. Different threads may share one interpreter or each take a different one.

Loosely put, picture the threads-plus-interpreters pairing as threads where sharing is opt-in.

A major perk: interpreters are isolated enough that they don’t share the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL), so pairing threads with several interpreters unlocks full multi-core parallelism. (That’s held true since Python 3.12.)

[Subject index](INDEX.md) · [Previous](running-in-an-interpreter.md) · [Continue](communication-between-interpreters.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)

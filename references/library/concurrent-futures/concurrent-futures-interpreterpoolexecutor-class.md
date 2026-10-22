# InterpreterPoolExecutor

### InterpreterPoolExecutor

Added in version 3.14.

To run calls asynchronously, the `InterpreterPoolExecutor` class relies on a pool of interpreters. Because it subclasses `ThreadPoolExecutor`, every worker still lives inside its own thread. What sets it apart is that each worker owns a separate interpreter and executes every task through it.

True multi-core parallelism is the foremost advantage of leaning on interpreters rather than threads alone. Since every interpreter carries its own [Global Interpreter Lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock), code in one interpreter can occupy one CPU core while code in a second interpreter proceeds unimpeded on a separate core.

What you give up is that authoring concurrent code spanning multiple interpreters may demand additional work. Yet that demand arises precisely because it pushes you to be intentional about when and how interpreters interact, and to spell out exactly which data passes between them. The payoff includes several upsides that offset that added work, among them true multi-core parallelism ? for instance, code structured this way can be simpler to reason about with respect to concurrency. A further sizeable upside is that you sidestep many of the notorious headaches of threads, such as race conditions.

Every worker's interpreter stands apart from all the rest. Calling them ?Isolated? means each one keeps its own runtime state and runs fully on its own. As an illustration, redirecting [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) inside one interpreter won't carry over automatically into any other. Importing a module in one interpreter doesn't import it automatically elsewhere; you'd have to import that module on its own in whichever interpreter needs it. Indeed, every module brought into one interpreter is an entirely distinct object from the matching module in a different interpreter, [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys), [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins), and even `__main__` included.

Because of this isolation, a mutable object ? or any other data ? can't be touched by more than one interpreter simultaneously. What that amounts to is that interpreters can't genuinely share such objects or data at all. Each interpreter must instead keep its own copy, and you'll be responsible for synchronizing any edits across those copies by hand. Such constraints don't apply to immutable objects and data, including the builtin singletons, strings, and tuples made of immutable objects.

The most effective way to communicate and synchronize across interpreters is with purpose-built tools, of the kind put forward in [**PEP 734**](https://peps.python.org/pep-0734/). A less efficient route is to serialize via [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) and then push the resulting bytes across a shared [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) or [`pipe`](https://docs.python.org/3.14/library/os.html#os.pipe).

 *class *concurrent.futures.InterpreterPoolExecutor(*max_workers=None*, *thread_name_prefix=''*, *initializer=None*, *initargs=()*)

A subclass of `ThreadPoolExecutor` that runs calls asynchronously on a pool of no more than *max_workers* threads. Every thread executes its tasks inside its own interpreter. Those worker interpreters stand apart from one another, so each keeps its own runtime state and none of them can share any mutable objects or other data. Every interpreter holds its own [Global Interpreter Lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock), so code executed through this executor enjoys true multi-core parallelism.

The optional *initializer* and *initargs* arguments carry the same sense they do for `ThreadPoolExecutor`: the initializer fires as each worker comes into being, except that here it fires within the worker's interpreter. To deliver them to that interpreter, the executor serializes *initializer* and *initargs* with [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle).

Note

Uncaught exceptions from *initializer* may be swapped out by the executor for [`ExecutionFailed`](https://docs.python.org/3.14/library/concurrent.interpreters.html#concurrent.interpreters.ExecutionFailed).

The other caveats inherited from the parent `ThreadPoolExecutor` hold here as well.

Both `submit()` and `map()` operate as usual, save that the worker serializes the callable plus its arguments with [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) before delivering them to its interpreter. In the same fashion, the worker serializes the returned value on the way back.

Whenever a worker's active task throws an uncaught exception, the worker always strives to keep that exception intact. When that works, it additionally points `__cause__` at a matching [`ExecutionFailed`](https://docs.python.org/3.14/library/concurrent.interpreters.html#concurrent.interpreters.ExecutionFailed) instance carrying a recap of the original exception. On the rare occasion the worker can't keep the original intact, it instead preserves the matching `ExecutionFailed` instance directly.

[Subject index](INDEX.md) · [Previous](threadpoolexecutor-example.md) · [Continue](concurrent-futures-processpoolexecutor-class.md)

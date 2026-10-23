# asyncio`asyncio` - Asynchronous I/O - Section introduction and initial examples

## asyncio - Asynchronous I/O

### `asyncio` - Asynchronous I/O

---

asyncio is a library for composing **concurrent** code by means of the **async/await** syntax.

Numerous Python asynchronous frameworks build on asyncio as their base, delivering high-performance network and web-servers, database connection libraries, distributed task queues, and the like.

For IO-bound work and high-level **structured** network code, asyncio is frequently an ideal match.

See also

[A Conceptual Overview of asyncio](https://docs.python.org/3.14/howto/a-conceptual-overview-of-asyncio.html#a-conceptual-overview-of-asyncio)

A walkthrough of asyncio's core ideas.

asyncio supplies a collection of **high-level** APIs that let you:

- [run Python coroutines](https://docs.python.org/3.14/library/asyncio-task.html#coroutine) side by side while retaining complete command over how they run;

- perform [network IO and IPC](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-streams);

- control [subprocesses](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio-subprocess);

- distribute tasks via [queues](https://docs.python.org/3.14/library/asyncio-queue.html#asyncio-queues);

- [synchronize](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio-sync) concurrent code;

On top of that, **low-level** APIs exist so that *library and framework developers* can:

- build and oversee [event loops](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio-event-loop), which expose asynchronous APIs covering [networking](https://docs.python.org/3.14/library/asyncio-eventloop.html#loop-create-server), the launching of [subprocesses](https://docs.python.org/3.14/library/asyncio-eventloop.html#loop-subprocess-exec), the handling of [OS signals](https://docs.python.org/3.14/library/asyncio-eventloop.html#loop-add-signal-handler), and so forth;

- implement efficient protocols using [transports](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-transports-protocols);

- [bridge](https://docs.python.org/3.14/library/asyncio-future.html#asyncio-futures) callback-based libraries and code with async/await syntax.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either non-functional or absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

asyncio REPL

The [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) lets you tinker with an `asyncio` concurrent context:

```pycon
$ python -m asyncio
asyncio REPL ...
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
'hello'

```

Compatibility between this REPL and [`PYTHON_BASIC_REPL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_BASIC_REPL) is only partial. For full functionality and the newest features, the default REPL is the recommended choice.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.run_stdin` with no arguments.

Changed in version 3.12.5: (also 3.11.10, 3.10.15, 3.9.20, and 3.8.20) Emits audit events.

Changed in version 3.13: Falls back on PyREPL where available; under that path [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) runs as well. Audit events are emitted.

Reference

High-level APIs

[Subject index](INDEX.md) · [Continue](asyncio-asynchronous-i-o-contract-runners.md)

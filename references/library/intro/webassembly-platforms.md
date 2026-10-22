# WebAssembly platforms

### WebAssembly platforms

A subset of POSIX APIs is offered by the [WebAssembly](https://webassembly.org/) platforms `wasm32-emscripten` ([Emscripten](https://emscripten.org/)) and `wasm32-wasi` ([WASI](https://wasi.dev/)). Because browsers and WebAssembly runtimes run sandboxed, their reach into the host and outside resources stays limited. Whenever a Python standard library module relies on processes, threading, networking, signals, or any other inter-process communication (IPC) mechanism, that module is either missing or behaves unlike it would on other Unix-like systems. Likewise restricted are File I/O, the file system, and the Unix permission-related functions. Blocking I/O is something Emscripten forbids. Further blocking calls such as [`sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) will stall the browser event loop.

How Python looks and acts on WebAssembly platforms is governed by the [Emscripten](https://emscripten.org/)-SDK or [WASI](https://wasi.dev/)-SDK version, the WASM runtimes in play (browser, NodeJS, [wasmtime](https://wasmtime.dev/)), plus Python's build-time flags. Since WebAssembly, Emscripten, and WASI remain standards in flux, certain capabilities — networking among them — may arrive down the road.

Anyone aiming to run Python inside the browser ought to look at [Pyodide](https://pyodide.org/) or [PyScript](https://pyscript.net/). The foundation under PyScript is Pyodide, and Pyodide in turn rests on CPython and Emscripten. Through Pyodide you reach the browsers’ JavaScript and DOM APIs, plus some networking by way of JavaScript’s `XMLHttpRequest` and `Fetch` APIs.

- Process-oriented APIs are absent or invariably fail with an error. Covered by this are APIs that launch fresh processes ([`fork()`](https://docs.python.org/3.14/library/os.html#os.fork), [`execve()`](https://docs.python.org/3.14/library/os.html#os.execve)), block on processes ([`waitpid()`](https://docs.python.org/3.14/library/os.html#os.waitpid)), deliver signals ([`kill()`](https://docs.python.org/3.14/library/os.html#os.kill)), or interact with processes in any other fashion. You can import [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess), but it won't function.

- While the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module is present, it is constrained and acts differently than on other platforms. Under Emscripten, sockets stay non-blocking at all times and need extra JavaScript code plus server-side helpers to tunnel TCP over WebSockets; consult [Emscripten Networking](https://emscripten.org/docs/porting/networking.html) for further details. WASI snapshot preview 1 allows sockets solely from a file descriptor that already exists.

- A handful of functions are stubs that simply do nothing and forever return hardcoded values.

- Functions dealing with file descriptors, file permissions, file ownership, and links are constrained and lack support for certain operations. WASI, for instance, won't allow symlinks whose file names are absolute.

[Subject index](INDEX.md) · [Previous](notes-on-availability.md) · [Continue](mobile-platforms.md)

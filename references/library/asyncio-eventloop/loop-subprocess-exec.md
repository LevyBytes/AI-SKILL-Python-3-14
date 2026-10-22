# Running subprocesses — Signature and initial contract

*async *loop.subprocess_exec(*protocol_factory*, **args*, *stdin=subprocess.PIPE*, *stdout=subprocess.PIPE*, *stderr=subprocess.PIPE*, ***kwargs*)

Launch a subprocess built from one or more string arguments handed in through *args*.

Each entry of *args* has to be a string of one of these forms:

- [`str`](https://docs.python.org/3.14/library/stdtypes.html#str);

- or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), encoded to the [filesystem encoding](https://docs.python.org/3.14/library/os.html#filesystem-encoding).

The leading string names the program executable, while the strings that follow supply its arguments. Taken together, these string arguments make up the program's `argv`.

This parallels the standard library [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) class invoked with `shell=False` and the string list given as its first argument; the difference is that `Popen` accepts that one list-of-strings argument, whereas *subprocess_exec* receives the strings as separate arguments.

The *protocol_factory* must be a callable returning a subclass of the [`asyncio.SubprocessProtocol`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.SubprocessProtocol) class.

Other parameters:

- *stdin* can be any of these:

  - a file-like object

  - an existing file descriptor (a positive integer), for example those created with [`os.pipe()`](https://docs.python.org/3.14/library/os.html#os.pipe)

  - the [`subprocess.PIPE`](https://docs.python.org/3.14/library/subprocess.html#subprocess.PIPE) constant (the default), which opens a fresh pipe and wires it up,

  - a `None` value, under which the subprocess inherits this process's own file descriptor

  - the [`subprocess.DEVNULL`](https://docs.python.org/3.14/library/subprocess.html#subprocess.DEVNULL) constant, signaling that the dedicated [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) file is to be used

- *stdout* can be any of these:

  - a file-like object

  - the [`subprocess.PIPE`](https://docs.python.org/3.14/library/subprocess.html#subprocess.PIPE) constant (default), creating a brand-new pipe and attaching it,

  - passing `None`, in which case the file descriptor of this process is inherited by the subprocess

  - the [`subprocess.DEVNULL`](https://docs.python.org/3.14/library/subprocess.html#subprocess.DEVNULL) constant, which routes the stream to the special [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) file

- *stderr* can be any of these:

  - a file-like object

  - the [`subprocess.PIPE`](https://docs.python.org/3.14/library/subprocess.html#subprocess.PIPE) constant (default), which spins up a new pipe and links it,

  - a `None` value, letting the subprocess take on the file descriptor of this process

  -

[Subject index](INDEX.md) · [Previous](running-subprocesses.md) · [Continue](subprocess-devnull-stream-contract.md) · [Owning module, declaration or section: Running subprocesses](running-subprocesses.md)

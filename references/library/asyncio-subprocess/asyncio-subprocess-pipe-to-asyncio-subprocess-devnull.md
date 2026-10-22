# Constants

### Constants

 asyncio.subprocess.PIPE

Can be passed to the *stdin*, *stdout* or *stderr* parameters.

Where *PIPE* gets passed to the *stdin* argument, the `Process.stdin` attribute will reference a [`StreamWriter`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamWriter) instance.

Where *PIPE* gets passed to the *stdout* or *stderr* arguments, the `Process.stdout` and `Process.stderr` attributes will reference [`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader) instances.

 asyncio.subprocess.STDOUT

A special value usable as the *stderr* argument, signalling that standard error ought to be funneled into standard output.

 asyncio.subprocess.DEVNULL

A special value usable as the *stdin*, *stdout* or *stderr* argument to the process-creation functions. It signals that the special file [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) will serve as the matching subprocess stream.

[Subject index](INDEX.md) · [Previous](subprocess-exec-and-shell-creation.md) · [Continue](asyncio-subprocess-process-class.md)

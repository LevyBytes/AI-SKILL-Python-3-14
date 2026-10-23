# signal - Note on SIGPIPE

### Note on SIGPIPE

When you pipe your program's output into utilities such as *[head(1)](https://manpages.debian.org/head(1))*, a `SIGPIPE` signal reaches your process as soon as the reader on the far end of standard output shuts the pipe early. The fallout is an exception along the lines of `BrokenPipeError: [Errno 32] Broken pipe`. To cope with it, surround your entry point so that this exception is caught, like so:

```python
import os
import sys

def main():
    try:
        # simulate large output (your code replaces this loop)
        for x in range(10000):
            print("y")
        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.
        sys.stdout.flush()
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE

if __name__ == '__main__':
    main()

```

Resist the temptation to flip `SIGPIPE`'s disposition back to `SIG_DFL` just to dodge [`BrokenPipeError`](https://docs.python.org/3.14/library/exceptions.html#BrokenPipeError). Going that route would make your program quit without warning any time a socket connection drops while you are still writing data to it.

[Subject index](INDEX.md) · [Previous](examples.md) · [Continue](note-on-signal-handlers-and-exceptions.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)

# Examples

### Examples

An example that drives a subprocess with the `Process` class and reads from its standard output through the [`StreamReader`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.StreamReader) class.

The subprocess is created by the `create_subprocess_exec()` function:

```python
import asyncio
import sys

async def get_date():
    code = 'import datetime as dt; print(dt.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line

date = asyncio.run(get_date())
print(f"Current date: {date}")

```

See also the [same example](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-subprocess-proto) written using low-level APIs.

[Subject index](INDEX.md) · [Previous](subprocess-and-threads.md)

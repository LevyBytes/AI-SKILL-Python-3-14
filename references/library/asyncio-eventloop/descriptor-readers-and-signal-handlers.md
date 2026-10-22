# Event-loop descriptor readers and signal handlers

```python
import asyncio
from socket import socketpair

# Create a pair of connected file descriptors
rsock, wsock = socketpair()

loop = asyncio.new_event_loop()

def reader():
    data = rsock.recv(100)
    print("Received:", data.decode())

    # We are done: unregister the file descriptor
    loop.remove_reader(rsock)

    # Stop the event loop
    loop.stop()

# Register the file descriptor for read event
loop.add_reader(rsock, reader)

# Simulate the reception of data from the network
loop.call_soon(wsock.send, 'abc'.encode())

try:
    # Run the event loop
    loop.run_forever()
finally:
    # We are done. Close sockets and the event loop.
    rsock.close()
    wsock.close()
    loop.close()

```

See also

- A comparable [example](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio-example-create-connection) that relies on transports, protocols, and the `loop.create_connection()` method.

- Yet another comparable [example](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio-example-create-connection-streams) built on streams and the high-level [`asyncio.open_connection()`](https://docs.python.org/3.14/library/asyncio-stream.html#asyncio.open_connection) function.

### Set signal handlers for SIGINT and SIGTERM

(Note that this `signal` example runs on Unix only.)

Attach handlers for the [`SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) and [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) signals via the `loop.add_signal_handler()` method:

```python
import asyncio
import functools
import os
import signal

def ask_exit(signame, loop):
    print("got signal %s: exit" % signame)
    loop.stop()

async def main():
    loop = asyncio.get_running_loop()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(
            getattr(signal, signame),
            functools.partial(ask_exit, signame, loop))

    await asyncio.sleep(3600)

print("Event loop running for 1 hour, press Ctrl+C to interrupt.")
print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

asyncio.run(main())

```

[Subject index](INDEX.md)

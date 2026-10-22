# signal — Note on Signal Handlers and Exceptions

### Note on Signal Handlers and Exceptions

Whenever a signal handler throws an exception, that exception travels up into the main thread and can surface following any [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) instruction. The clearest case is a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt), which can pop up at any moment as the program runs. The bulk of Python code, the standard library included, cannot be hardened against this, so a `KeyboardInterrupt` (or any other exception thrown from a handler) may occasionally leave the program in a state nobody anticipated.

To make the problem concrete, look at the snippet below:

```python
class SpamContext:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        # If KeyboardInterrupt occurs here, everything is fine
        self.lock.acquire()
        # If KeyboardInterrupt occurs here, __exit__ will not be called
        ...
        # KeyboardInterrupt could occur just before the function returns

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
        self.lock.release()

```

Plenty of programs, particularly ones that just want to quit when a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) arrives, will not care about this, yet intricate or high-reliability software ought to steer clear of raising exceptions inside signal handlers. Such software should likewise not lean on catching `KeyboardInterrupt` to shut down cleanly. The better route is to register a dedicated `SIGINT` handler. The following shows an HTTP server written to sidestep `KeyboardInterrupt`:

```python
import signal
import socket
from selectors import DefaultSelector, EVENT_READ
from http.server import HTTPServer, SimpleHTTPRequestHandler

interrupt_read, interrupt_write = socket.socketpair()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    interrupt_write.send(b'\0')
signal.signal(signal.SIGINT, handler)

def serve_forever(httpd):
    sel = DefaultSelector()
    sel.register(interrupt_read, EVENT_READ)
    sel.register(httpd, EVENT_READ)

    while True:
        for key, _ in sel.select():
            if key.fileobj == interrupt_read:
                interrupt_read.recv(1)
                return
            if key.fileobj == httpd:
                httpd.handle_request()

print("Serving on port 8000")
httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
serve_forever(httpd)
print("Shutdown...")

```

[Subject index](INDEX.md) · [Previous](note-on-sigpipe.md) · [Owning module, declaration or section: signal](signal-set-handlers-for-asynchronous-events.md)

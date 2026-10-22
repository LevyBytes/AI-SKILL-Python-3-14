# threading: `threading.Barrier`

### Barrier objects

Added in version 3.2.

This class offers a basic synchronization primitive for use by a fixed count of threads that have to wait for one another. Each thread tries to clear the barrier by invoking the `wait()` method and will block until every one of the threads has issued its `wait()` call. At that moment, the threads are freed all at once.

The barrier may be reused as many times as you like for the same count of threads.

By way of example, here is a basic way to coordinate a client and server thread:

```python
b = Barrier(2, timeout=5)

def server():
    start_server()
    b.wait()
    while True:
        connection = accept_connection()
        process_server_connection(connection)

def client():
    b.wait()
    while True:
        connection = make_connection()
        process_client_connection(connection)

```

 *class *threading.Barrier(*parties*, *action=None*, *timeout=None*)

Build a barrier object for *parties* number of threads. An *action*, when supplied, is a callable that one of the threads invokes upon their release. *timeout* is the default timeout value applied if none gets specified for the `wait()` method.

[Subject index](INDEX.md) · [Previous](threading-timer-cancel.md) · [Continue](threading-barrier-wait-to-threading-barrier-abort.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)

# multiprocessing — Listeners and Clients — Signature and initial contract

multiprocessing.connection.wait(*object_list*, *timeout=None*)

Wait until an object within *object_list* turns ready. Gives back the list of those *object_list* objects that are ready. When *timeout* is a float, the call blocks for no more than that many seconds. When *timeout* is `None`, it blocks without limit. A negative timeout matches a zero timeout.

On both POSIX and Windows, an object may appear within *object_list* when it is

- a readable `Connection` object;

- a connected and readable [`socket.socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) object; or

- the `sentinel` attribute of a `Process` object.

A connection or socket object turns ready once data is on hand to read from it, or the far end has closed.

**POSIX**: `wait(object_list, timeout)` is almost the same as `select.select(object_list, [], [], timeout)`. The distinction is that, when [`select.select()`](https://docs.python.org/3.14/library/select.html#select.select) is interrupted by a signal, it may raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) carrying an error number of `EINTR`, while `wait()` will not.

**Windows**: An entry in *object_list* has to be either an integer handle that is waitable (per the definition the documentation of the Win32 function `WaitForMultipleObjects()` uses) or an object carrying a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method that gives back either a socket handle or a pipe handle. (Note that neither pipe handles nor socket handles count as waitable handles.)

Added in version 3.3.

**Examples**

The server code below brings up a listener whose authentication key is `'secret password'`. It then holds for a connection and pushes a bit of data over to the client:

```python
from multiprocessing.connection import Listener
from array import array

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

with Listener(address, authkey=b'secret password') as listener:
    with listener.accept() as conn:
        print('connection accepted from', listener.last_accepted)

        conn.send([2.25, None, 'junk', float])

        conn.send_bytes(b'hello')

        conn.send_bytes(array('i', [42, 1729]))

```

The code below connects to the server and takes in a bit of data from it:

```python
from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'secret password') as conn:
    print(conn.recv())                  # => [2.25, None, 'junk', float]

    print(conn.recv_bytes())            # => 'hello'

    arr = array('i', [0, 0, 0, 0, 0])
    print(conn.recv_bytes_into(arr))    # => 8
    print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

```

The code below leans on `wait()` to await messages from several processes together:

[Subject index](INDEX.md) · [Previous](connection-listener-lifecycle.md) · [Continue](pipe-connection-wait-example.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.connection.Listener](connection-listener-lifecycle.md) · [Owning module, declaration or section: Listeners and Clients](connection-authentication-and-client.md)

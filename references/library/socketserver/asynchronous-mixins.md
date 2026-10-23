# socketserver - Asynchronous Mixins

### Asynchronous Mixins

For building asynchronous handlers, reach for the `ThreadingMixIn` and `ForkingMixIn` classes.

An example for the `ThreadingMixIn` class:

The complete program is in the [upstream source](https://docs.python.org/3.14/library/socketserver.html#asynchronous-mixins).

Running the example should give you output along these lines:

```shell
$ python ThreadedTCPServer.py
Server loop running in thread: Thread-1
Received: Thread-2: Hello World 1
Received: Thread-3: Hello World 2
Received: Thread-4: Hello World 3

```

The `ForkingMixIn` class works the same way, save that the server forks a fresh process for every request. Available only on POSIX platforms that support [`fork()`](https://docs.python.org/3.14/library/os.html#os.fork).

[Subject index](INDEX.md) · [Previous](socketserver-udpserver-example.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md)

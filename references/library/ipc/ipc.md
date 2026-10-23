# Ipc

# Ipc

### Networking and Interprocess Communication

Covered throughout this chapter are modules that supply the machinery for networking together with inter-processes communication.

A handful are limited to a pair of processes sharing one machine — take [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) and [`mmap`](https://docs.python.org/3.14/library/mmap.html#module-mmap), for instance. The rest implement networking protocols, letting two or more processes talk to one another even when spread across separate machines.

Here is the roster of modules this chapter walks through:

- [`asyncio` - Asynchronous I/O](https://docs.python.org/3.14/library/asyncio.html)
- [`socket` - Low-level networking interface](https://docs.python.org/3.14/library/socket.html)
- [`ssl` - TLS/SSL wrapper for socket objects](https://docs.python.org/3.14/library/ssl.html)
- [`select` - Waiting for I/O completion](https://docs.python.org/3.14/library/select.html)
- [`selectors` - High-level I/O multiplexing](https://docs.python.org/3.14/library/selectors.html)
- [`signal` - Set handlers for asynchronous events](https://docs.python.org/3.14/library/signal.html)
- [`mmap` - Memory-mapped file support](https://docs.python.org/3.14/library/mmap.html)

[Subject index](INDEX.md)

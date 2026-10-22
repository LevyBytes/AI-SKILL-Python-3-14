# IPC

### IPC

Wanting quick IPC between a pair of processes on the same box, your better bets are pipes or shared memory. And if you go with AF_INET sockets regardless, tie the “server” socket to `'localhost'`. Across most platforms that lets you sidestep a layer or two of network plumbing and gains you a fair bit of speed.

See also

The [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) wraps cross-platform IPC up inside a more elevated API.

[Subject index](INDEX.md) · [Previous source context](creating-a-socket.md) · [Following source context](using-a-socket.md)

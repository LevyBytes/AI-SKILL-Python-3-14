# multiprocessing — Listeners and Clients — Code example: from multiprocessing import Process, Pipe, current_process

```python
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait

def foo(w):
    for i in range(10):
        w.send((i, current_process().name))
    w.close()

if __name__ == '__main__':
    readers = []

    for i in range(4):
        r, w = Pipe(duplex=False)
        readers.append(r)
        p = Process(target=foo, args=(w,))
        p.start()
        # We close the writable end of the pipe now to be sure that
        # p is the only process which owns a handle for it.  This
        # ensures that when p closes its handle for the writable end,
        # wait() will promptly report the readable end as being ready.
        w.close()

    while readers:
        for r in wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg)

```

[Subject index](INDEX.md) · [Previous](multiprocessing-connection-wait.md) · [Continue](address-formats.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.connection.Listener](connection-listener-lifecycle.md) · [Owning module, declaration or section: Listeners and Clients](connection-authentication-and-client.md) · [Owning module, declaration or section: multiprocessing.connection.wait](multiprocessing-connection-wait.md)

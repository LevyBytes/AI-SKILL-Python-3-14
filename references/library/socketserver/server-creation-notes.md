# socketserver: Server mixin close behavior and concurrency notes

block_on_close

`ForkingMixIn.server_close` holds until every child process is done, unless the `block_on_close` attribute is `False`.

`ThreadingMixIn.server_close` holds until every non-daemon thread is done, unless the `block_on_close` attribute is `False`.

 max_children

Sets the number of child processes that `ForkingMixIn` keeps active for servicing requests simultaneously. Should that ceiling be hit, incoming requests wait for a child process to wrap up.

 daemon_threads

For `ThreadingMixIn`, enable daemonic threads by assigning `True` to `ThreadingMixIn.daemon_threads` so the server does not wait on the threads to finish.

Changed in version 3.7: `ForkingMixIn.server_close` along with `ThreadingMixIn.server_close` will now block until every child process plus each non-daemonic thread has finished. A fresh `ForkingMixIn.block_on_close` class attribute lets you opt back into the behaviour from before 3.7.

[Subject index](INDEX.md) · [Previous](forking-and-threading-server-mixins.md) · [Continue](concurrent-tcp-udp-and-unix-server-classes.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md) · [Owning module, declaration or section: socketserver.ForkingMixIn; socketserver.ThreadingMixIn](forking-and-threading-server-mixins.md) · [Owning module, declaration or section: Server Creation Notes](forking-and-threading-server-mixins.md)

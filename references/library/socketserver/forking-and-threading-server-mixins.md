# socketserver: `socketserver.ForkingMixIn`, `socketserver.ThreadingMixIn`

### Server Creation Notes

The inheritance diagram contains five classes, four of which stand for synchronous servers of four kinds:

```python
+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+

```

Observe that `UnixDatagramServer` inherits from `UDPServer` rather than from `UnixStreamServer` — what distinguishes an IP server from a Unix one is solely the address family.

 *class *socketserver.ForkingMixIn

 *class *socketserver.ThreadingMixIn

You can produce forking and threading variants of every server type with these mix-in classes. As an illustration, here is how `ThreadingUDPServer` gets defined:

```python
class ThreadingUDPServer(ThreadingMixIn, UDPServer):
    pass

```

The mix-in class is listed first because it supersedes a method that `UDPServer` defines. Adjusting the assorted attributes likewise alters how the server machinery underneath operates.

`ForkingMixIn`, along with the Forking classes noted further down, work solely on POSIX platforms that provide [`fork()`](https://docs.python.org/3.14/library/os.html#os.fork).

[Subject index](INDEX.md) · [Previous](unix-stream-and-datagram-servers.md) · [Continue](server-creation-notes.md) · [Owning module, declaration or section: socketserver](socketserver-tcpserver-class.md)

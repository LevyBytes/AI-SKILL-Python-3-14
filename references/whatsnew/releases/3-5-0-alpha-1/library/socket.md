# Python 3.5.0 alpha 1 / library / socket

[bpo-21032](https://bugs.python.org/issue?@action=redirect&bpo=21032): A socket leak was fixed for when HTTPConnection.getresponse() fails. Martin Panter wrote the first patch.

[bpo-20951](https://bugs.python.org/issue?@action=redirect&bpo=20951): On a non-blocking socket, SSLSocket.send() now signals either SSLWantReadError or SSLWantWriteError whenever the call would block. Earlier behavior returned 0 instead. Nikolaus Rath provided the patch.

[bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552): A fresh socket.sendfile() method lets a file travel across a socket by leveraging the high-performance os.sendfile() under UNIX. Giampaolo Rodola? wrote the patch.

[bpo-20173](https://bugs.python.org/issue?@action=redirect&bpo=20173): The sha1, sha256, sha512 and md5 routines were ported to ArgumentClinic. Vajrasky Kok wrote the patch.

- On 64-bit Windows, repr(_socket.socket) was fixed so it no longer raises OverflowError when the socket is closed. repr(socket.socket) was already fine.

[bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043): The function time.monotonic() can now be relied on everywhere. When a timeout is in effect, `threading.Lock.acquire()`, `threading.RLock.acquire()`, and socket calls draw on a monotonic clock rather than the system clock.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.14.3 final / library / build and platforms

[gh-143249](https://github.com/python/cpython/issues/143249): Possible buffer leaks during error handling in Windows overlapped I/O are now fixed.

[gh-142991](https://github.com/python/cpython/issues/142991): Socket operations like recvfrom() and sendto() were fixed for the FreeBSD divert(4) socket.

[gh-139262](https://github.com/python/cpython/issues/139262): On Windows, the fresh `PyREPL` could drop some keystrokes, particularly in combination with the ALT key. Chris Eibl provided the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

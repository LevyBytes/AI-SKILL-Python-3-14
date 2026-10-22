# hashlib — File hashing

### File hashing

A convenience function for hashing a file or file-like object efficiently is part of the hashlib module.

 hashlib.file_digest(*fileobj*, *digest*, */*)

Hand back a digest object that has already taken in the contents of the file object.

*fileobj* has to be a file-like object opened for reading in binary mode. Acceptable inputs include file objects from builtin [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) instances, SocketIO objects produced by [`socket.socket.makefile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.makefile), and the like. *fileobj* has to be opened in blocking mode, or else a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) may be raised.

The function might sidestep Python’s I/O and work straight through the file descriptor from [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno). Treat *fileobj* as being in an unknown state once this function returns or raises. Closing *fileobj* falls to the caller.

*digest* is required to be one of: a hash algorithm name given as a *str*, a hash constructor, or any callable yielding a hash object.

Example:

```python
>>> import io, hashlib, hmac
>>> with open("library/hashlib.rst", "rb") as f:
...     digest = hashlib.file_digest(f, "sha256")
...
>>> digest.hexdigest()
'...'

```

```python
>>> buf = io.BytesIO(b"somedata")
>>> mac1 = hmac.HMAC(b"key", digestmod=hashlib.sha512)
>>> digest = hashlib.file_digest(buf, lambda: mac1)

```

```python
>>> digest is mac1
True
>>> mac2 = hmac.HMAC(b"key", b"somedata", digestmod=hashlib.sha512)
>>> mac1.digest() == mac2.digest()
True

```

Added in version 3.11.

Changed in version 3.14: A [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) is now raised when the file sits in non-blocking mode. Earlier releases instead tacked stray null bytes onto the digest.

[Subject index](INDEX.md) · [Previous](hashlib-shake-128-to-shake-hexdigest.md) · [Continue](hashlib-pbkdf2-hmac-to-hashlib-scrypt.md) · [Owning module, declaration or section: hashlib](hashlib-secure-hashes-and-message-digests.md)

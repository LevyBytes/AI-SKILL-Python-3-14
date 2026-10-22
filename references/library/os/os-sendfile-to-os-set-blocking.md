# os: `os.sendfile()`, `os.SF_NODISKIO`, `os.SF_MNOWAIT`, `os.SF_SYNC`, `os.SF_NOCACHE`, `os.set_blocking()`

os.sendfile(*out_fd*, *in_fd*, *offset*, *count*)

 os.sendfile(*out_fd*, *in_fd*, *offset*, *count*, *headers=()*, *trailers=()*, *flags=0*)

Copy *count* bytes out of file descriptor *in_fd* into file descriptor *out_fd*, beginning at *offset*. The count of bytes sent is returned. Once EOF arrives the result is `0`.

Every platform that defines `sendfile()` supports the first form of the call.

On Linux, when *offset* is supplied as `None`, bytes are taken from the current position of *in_fd*, and that position of *in_fd* advances.

The second form works on macOS plus FreeBSD; there *headers* and *trailers* are any sequences of buffers, emitted ahead of and following the data drawn from *in_fd*. Its return value matches the first form.

On macOS and FreeBSD, supplying `0` for *count* directs the call to keep sending until the end of *in_fd* arrives.

Sockets are accepted as the *out_fd* file descriptor on every platform, and a few platforms also permit other types (for instance a regular file or a pipe).

Cross-platform applications ought to avoid the *headers*, *trailers* and *flags* arguments.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Note

For a higher-level wrapper around `sendfile()`, consult [`socket.socket.sendfile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.sendfile).

Added in version 3.3.

Changed in version 3.9: The parameters *out* and *in* were renamed to *out_fd* and *in_fd*.

 os.SF_NODISKIO

 os.SF_MNOWAIT

 os.SF_SYNC

Arguments accepted by the `sendfile()` function, where the implementation supports them.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.3.

 os.SF_NOCACHE

Argument accepted by the `sendfile()` function, where the implementation supports it. The data avoids being held in virtual memory and is released afterward.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.11.

 os.set_blocking(*fd*, *blocking*, */*)

Configure the blocking mode of the given file descriptor. Apply the `O_NONBLOCK` flag when blocking is `False`, and remove the flag otherwise.

Refer also to `get_blocking()` and [`socket.socket.setblocking()`](https://docs.python.org/3.14/library/socket.html#socket.socket.setblocking).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

This function is restricted on WASI; consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

On Windows, the function only works with pipes.

Added in version 3.5.

Changed in version 3.12: Added pipe support on Windows.

[Subject index](INDEX.md) · [Previous](os-rwf-dsync-to-os-readinto.md) · [Continue](os-splice-to-os-unlockpt.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)

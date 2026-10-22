# os: `os.uname()`, `os.unsetenv()`, `os.unshare()`

os.uname()

Give back information that identifies the operating system now running. What comes back is an object carrying five attributes:

- `sysname` - operating system name

- `nodename` - name of machine on network (implementation-defined)

- `release` - operating system release

- `version` - operating system version

- `machine` - hardware identifier

To preserve backwards compatibility, this object is iterable too, acting like a five-tuple holding `sysname`, `nodename`, `release`, `version`, and `machine` in that sequence.

Certain systems clip `nodename` down to 8 characters or to its leading component; a better route to the hostname is [`socket.gethostname()`](https://docs.python.org/3.14/library/socket.html#socket.gethostname) or even `socket.gethostbyaddr(socket.gethostname())`.

On macOS, iOS and Android, what comes back is the *kernel* name and version (that is, `'Darwin'` on macOS and iOS; `'Linux'` on Android). [`platform.uname()`](https://docs.python.org/3.14/library/platform.html#platform.uname) is available to fetch the user-facing operating system name and version on iOS and Android.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.3: The return type went from a plain tuple to a tuple-like object whose attributes are named.

 os.unsetenv(*key*, */*)

Clear (remove) the environment variable whose name is *key*. Environment changes of this kind reach subprocesses launched with `os.system()`, `popen()` or `fork()` and `execv()`.

Removing items from `os.environ` automatically translates into a matching call to `unsetenv()`; calls to `unsetenv()`, however, don't update `os.environ`, so deleting items of `os.environ` is in fact preferable.

See also the `os.reload_environ()` function.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.unsetenv` with argument `key`.

Changed in version 3.9: The function is available at all times now, Windows included.

 os.unshare(*flags*)

Detach pieces of the process execution context, relocating them into a freshly built namespace. Consult the *[unshare(2)](https://manpages.debian.org/unshare(2))* man page for fuller detail. The *flags* argument is a bit mask, ORing together zero or more of the CLONE_* constants, that names which pieces of the execution context should be unshared from their current associations and moved into a new namespace. Should the *flags* argument be `0`, the calling process's execution context goes unchanged.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.16.

Added in version 3.12.

See also

The `setns()` function.

Flags handed to the `unshare()` function, where the implementation backs them. Consult *[unshare(2)](https://manpages.debian.org/unshare(2))* in the Linux manual for precisely what they do and where they are available.

[Subject index](INDEX.md) · [Previous](os-setpgrp-to-os-umask.md) · [Continue](os-clone-files-to-os-clone-vm.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md)

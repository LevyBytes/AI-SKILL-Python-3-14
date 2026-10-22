# msvcrt — File Operations

### File Operations

 msvcrt.locking(*fd*, *mode*, *nbytes*)

Place a lock on a portion of a file, identifying the file through the C runtime descriptor *fd*. A failure surfaces as [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). Starting at wherever the file pointer currently sits, the lock covers *nbytes* bytes onward and is permitted to run past where the file presently ends. The *mode* argument has to be one of the `LK_*` constants given below. You can hold locks on several stretches of a single file simultaneously, provided those stretches do not overlap. Locks that sit next to each other stay distinct rather than combining, so you release each one on its own.

Emits the [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `msvcrt.locking`, carrying the arguments `fd`, `mode`, `nbytes`.

 msvcrt.LK_LOCK

 msvcrt.LK_RLCK

Locks the bytes you name. Should the lock not take, a fresh attempt follows right away once 1 second has elapsed. When 10 such tries have all failed to secure the bytes, the call ends by raising [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 msvcrt.LK_NBLCK

 msvcrt.LK_NBRLCK

Locks the bytes you name. When the lock cannot be obtained, the result is an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 msvcrt.LK_UNLCK

Releases the bytes you name; they have to already be under a lock.

 msvcrt.setmode(*fd*, *flags*)

Choose how line endings are translated for the descriptor *fd*. Passing *flags* as [`os.O_TEXT`](https://docs.python.org/3.14/library/os.html#os.O_TEXT) selects text mode, whereas [`os.O_BINARY`](https://docs.python.org/3.14/library/os.html#os.O_BINARY) selects binary mode.

 msvcrt.open_osfhandle(*handle*, *flags*)

Turn the operating-system file handle *handle* into a C runtime descriptor. Build the *flags* argument by OR-ing together [`os.O_APPEND`](https://docs.python.org/3.14/library/os.html#os.O_APPEND), [`os.O_RDONLY`](https://docs.python.org/3.14/library/os.html#os.O_RDONLY), [`os.O_TEXT`](https://docs.python.org/3.14/library/os.html#os.O_TEXT) and [`os.O_NOINHERIT`](https://docs.python.org/3.14/library/os.html#os.O_NOINHERIT). Hand the resulting descriptor to [`os.fdopen()`](https://docs.python.org/3.14/library/os.html#os.fdopen) when you want a file object built around it.

Unless you say otherwise, the descriptor can be inherited; supply the [`os.O_NOINHERIT`](https://docs.python.org/3.14/library/os.html#os.O_NOINHERIT) flag to block that.

Emits the [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `msvcrt.open_osfhandle`, carrying the arguments `handle`, `flags`.

 msvcrt.get_osfhandle(*fd*)

Give back the operating-system file handle that corresponds to descriptor *fd*. An unrecognized *fd* triggers an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Emits the [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `msvcrt.get_osfhandle`, carrying the argument `fd`.

[Subject index](INDEX.md) · [Previous](msvcrt-useful-routines-from-the-ms-vc-runtime.md) · [Continue](msvcrt-kbhit-to-msvcrt-ungetwch.md) · [Owning module, declaration or section: msvcrt](msvcrt-useful-routines-from-the-ms-vc-runtime.md)

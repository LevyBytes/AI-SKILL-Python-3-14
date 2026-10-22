# os.timerfd_create

<a id="os--timer-file-descriptors"></a>

Timer File Descriptors: Added in version 3.13.

These functions deliver support for Linux's *timer file descriptor* API. As you would expect, every one of them is available on Linux alone.

 os.timerfd_create(*clockid*, */*, ***, *flags=0*)

Create and give back a timer file descriptor (*timerfd*).

The file descriptor that `timerfd_create()` gives back supports:

- `read()`

- [`select()`](https://docs.python.org/3.14/library/select.html#select.select)

- [`poll()`](https://docs.python.org/3.14/library/select.html#select.poll)

Read the integer file descriptor with `os.read(fd, 8)`. When the timer has already expired one or more times, `read()` gives back the count of expirations using the host's endianness, which may be turned into an [`int`](https://docs.python.org/3.14/library/functions.html#int) via `int.from_bytes(x, byteorder=sys.byteorder)`.

[`select()`](https://docs.python.org/3.14/library/select.html#select.select) and [`poll()`](https://docs.python.org/3.14/library/select.html#select.poll) can serve to wait until the timer expires and the file descriptor becomes readable.

*clockid* has to be a valid [clock ID](https://docs.python.org/3.14/library/time.html#time-clock-id-constants), as laid out in the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module:

- [`time.CLOCK_REALTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_REALTIME)

- [`time.CLOCK_MONOTONIC`](https://docs.python.org/3.14/library/time.html#time.CLOCK_MONOTONIC)

- [`time.CLOCK_BOOTTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_BOOTTIME) (Since Linux 3.15 for timerfd_create)

When *clockid* is [`time.CLOCK_REALTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_REALTIME), a settable system-wide real-time clock is used. Should the system clock change, the timer setting needs to be refreshed. To cancel a timer when the system clock changes, consult `TFD_TIMER_CANCEL_ON_SET`.

When *clockid* is [`time.CLOCK_MONOTONIC`](https://docs.python.org/3.14/library/time.html#time.CLOCK_MONOTONIC), a non-settable monotonically increasing clock is used. Even should the system clock change, the timer setting stays unaffected.

When *clockid* is [`time.CLOCK_BOOTTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_BOOTTIME), it behaves the same as [`time.CLOCK_MONOTONIC`](https://docs.python.org/3.14/library/time.html#time.CLOCK_MONOTONIC) except that it folds in any time during which the system is suspended.

You can adjust the file descriptor's behaviour by supplying a *flags* value. Any of the variables below may be used, joined together with bitwise OR (the `|` operator):

- `TFD_NONBLOCK`

- `TFD_CLOEXEC`

When `TFD_NONBLOCK` is not set as a flag, `read()` blocks until the timer expires. When it is set as a flag, `read()` does not block, but should no expiration have occurred since the last call to read, `read()` raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) with `errno` set to [`errno.EAGAIN`](https://docs.python.org/3.14/library/errno.html#errno.EAGAIN).

`TFD_CLOEXEC` is always set by Python automatically.

The file descriptor has to be closed with `os.close()` once it is no longer needed, or otherwise the file descriptor will be leaked.

See also

The *[timerfd_create(2)](https://manpages.debian.org/timerfd_create(2))* man page.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

[Subject index](INDEX.md) · [Set a timer](timerfd-settime.md) · [State and nanoseconds](timerfd-state-and-nanoseconds.md)

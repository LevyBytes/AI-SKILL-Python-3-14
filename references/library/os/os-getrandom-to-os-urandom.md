# os - Random numbers

### Random numbers

 os.getrandom(*size*, *flags=0*)

Get up to *size* random bytes. This function may return fewer bytes than were requested.

You can use these bytes to seed user-space random number generators or for cryptographic purposes.

`getrandom()` draws on entropy gathered from device drivers and other sources of environmental noise. Reading large amounts of data needlessly will hurt other users of the `/dev/random` and `/dev/urandom` devices.

The flags argument is a bit mask able to hold zero or more of these values ORed together: `os.GRND_RANDOM` and `GRND_NONBLOCK`.

See also the [Linux getrandom() manual page](https://man7.org/linux/man-pages/man2/getrandom.2.html).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.17.

Added in version 3.6.

 os.urandom(*size*, */*)

Return a bytestring of *size* random bytes fit for cryptographic use.

This function yields random bytes drawn from an OS-specific randomness source. The returned data ought to be unpredictable enough for cryptographic applications, though just how good it is rests on the OS implementation.

On Linux, where the `getrandom()` syscall is present, it runs in blocking mode: it blocks until the system urandom entropy pool has been initialized (the kernel gathers 128 bits of entropy). See [**PEP 524**](https://peps.python.org/pep-0524/) for the reasoning. On Linux, the `getrandom()` function can be used to obtain random bytes in non-blocking mode (via the `GRND_NONBLOCK` flag) or to poll until the system urandom entropy pool has been initialized.

On a Unix-like system, random bytes are read out of the `/dev/urandom` device. Where the `/dev/urandom` device is unavailable or not readable, the [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) exception is raised.

On Windows, it will use `BCryptGenRandom()`.

See also

The [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets) module supplies higher level functions. For a convenient interface to the random number generator your platform provides, please see [`random.SystemRandom`](https://docs.python.org/3.14/library/random.html#random.SystemRandom).

Changed in version 3.5: Where Linux 3.17 or later runs, the `getrandom()` syscall now gets used if it is present. Where OpenBSD 5.6 or later runs, the C `getentropy()` function now gets used. Both of these routines steer clear of an internal file descriptor.

Changed in version 3.5.2: On Linux, when the `getrandom()` syscall blocks (the urandom entropy pool has not been initialized yet), fall back to reading `/dev/urandom`.

Changed in version 3.6: Under Linux, `getrandom()` now runs in blocking mode so as to strengthen security.

Changed in version 3.11: On Windows, `BCryptGenRandom()` takes the place of `CryptGenRandom()`, which is deprecated.

[Subject index](INDEX.md) · [Previous](os-pathsep-to-os-rtld-deepbind.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)

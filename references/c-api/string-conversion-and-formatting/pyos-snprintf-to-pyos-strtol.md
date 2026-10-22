# string conversion and formatting C API: `PyOS_snprintf()`, `PyOS_vsnprintf()`, `PyOS_strtoul()`, `PyOS_strtol()`

# Conversion, Coro, Curses

## Overview

Covers: String conversion and formatting; Coroutine Objects; Curses C API.

## String conversion and formatting

### String conversion and formatting

Functions for number conversion and formatted string output.

 int PyOS_snprintf(char *str, size_t size, const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Write at most *size* bytes into *str*, laying them out per the *format* template along with the additional arguments supplied. Consult the Unix man page *[snprintf(3)](https://manpages.debian.org/snprintf(3))*.

 int PyOS_vsnprintf(char *str, size_t size, const char *format, va_list va)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Write at most *size* bytes into *str*, laying them out per the *format* template along with the *va* variable argument list. Unix man page *[vsnprintf(3)](https://manpages.debian.org/vsnprintf(3))*.

`PyOS_snprintf()` and `PyOS_vsnprintf()` are thin wrappers over the Standard C library functions `snprintf()` and `vsnprintf()`. They exist so that edge-case behavior stays predictable, something the Standard C versions fail to promise.

After they finish, the wrappers guarantee `str[size-1]` holds `'\0'`. The amount they emit into str never exceeds *size* bytes, counting the closing `'\0'`. Each one demands that `str != NULL`, `size > 0`, `format != NULL` and `size < INT_MAX`. Consequently there is no counterpart to the C99 `n = snprintf(NULL, 0, ...)` form that reports the buffer size you would need.

Read the result code (*rv*) these functions hand back according to these rules:

- A value of `0 <= rv < size` signals a successful conversion in which *rv* characters landed in *str*, not counting the terminating `'\0'` byte sitting at `str[rv]`.

- A value of `rv >= size` means the conversion got cut short; succeeding would have called for a buffer holding `rv + 1` bytes. Here `str[size-1]` equals `'\0'`.

- A value of `rv < 0` flags a failed conversion; `str[size-1]` again holds `'\0'`, though everything else in *str* is undefined. Which specific failure triggered this is decided by the host platform.

Below are the routines that turn strings into numbers without regard to the active locale.

 unsigned long PyOS_strtoul(const char *str, char **ptr, int base)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Read the leading portion of the `str` string as an unsigned long, interpreting it in the supplied `base`, where `base` lies from `2` through `36` inclusive or takes the distinguished value `0`.

Any leading whitespace, plus the letter case, gets skipped over. With `base` set to zero, the routine inspects a leading `0b`, `0o` or `0x` prefix to deduce the radix; lacking one, it falls back to `10`. Base is restricted to 0 or the 2-to-36 span (inclusive). Should `ptr` be non-`NULL`, it ends up holding a pointer marking where the scan stopped.

Should the parsed number exceed what the return type can represent, a range error fires (`errno` becomes `ERANGE`) and the call yields `ULONG_MAX`. When nothing at all can be parsed, it yields `0`.

See also the Unix man page *[strtoul(3)](https://manpages.debian.org/strtoul(3))*.

Added in version 3.2.

 long PyOS_strtol(const char *str, char **ptr, int base)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Read the leading portion of the `str` string as a long, interpreting it in the supplied `base`, where `base` lies from `2` through `36` inclusive or takes the distinguished value `0`.

Behaves like `PyOS_strtoul()`, except it produces a long and gives back `LONG_MAX` when an overflow happens.

See also the Unix man page *[strtol(3)](https://manpages.debian.org/strtol(3))*.

Added in version 3.2.

[Subject index](INDEX.md) · [Following source contract](pyos-string-to-double-to-pyos-strnicmp.md)

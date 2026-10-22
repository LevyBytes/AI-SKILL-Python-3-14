# os: Memory-backed file flags, huge pages and event descriptors

os.MFD_CLOEXEC

 os.MFD_ALLOW_SEALING

 os.MFD_HUGETLB

 os.MFD_HUGE_SHIFT

 os.MFD_HUGE_MASK

 os.MFD_HUGE_64KB

 os.MFD_HUGE_512KB

 os.MFD_HUGE_1MB

 os.MFD_HUGE_2MB

 os.MFD_HUGE_8MB

 os.MFD_HUGE_16MB

 os.MFD_HUGE_32MB

 os.MFD_HUGE_256MB

 os.MFD_HUGE_512MB

 os.MFD_HUGE_1GB

 os.MFD_HUGE_2GB

 os.MFD_HUGE_16GB

These flags can be handed to `memfd_create()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.17 with glibc >= 2.27

The `MFD_HUGE*` flags are available only since Linux 4.14.

Added in version 3.8.

 os.eventfd(*initval*[, *flags=os.EFD_CLOEXEC*])

Create and give back an event file descriptor. The file descriptors support raw `read()` and `write()` with a buffer size of 8, [`select()`](https://docs.python.org/3.14/library/select.html#select.select), [`poll()`](https://docs.python.org/3.14/library/select.html#select.poll) and the like. Consult the man page *[eventfd(2)](https://manpages.debian.org/eventfd(2))* for further information. By default, the new file descriptor is non-inheritable.

*initval* is the starting value of the event counter. The starting value has to be a 32 bit unsigned integer. Note that the starting value is capped at a 32 bit unsigned int even though the event counter is an unsigned 64 bit integer whose maximum value is 264-2.

*flags* can be assembled from `EFD_CLOEXEC`, `EFD_NONBLOCK`, and `EFD_SEMAPHORE`.

When `EFD_SEMAPHORE` is given and the event counter is non-zero, `eventfd_read()` gives back 1 and lowers the counter by one.

When `EFD_SEMAPHORE` is not given and the event counter is non-zero, `eventfd_read()` gives back the current event counter value and resets the counter to zero.

When the event counter is zero and `EFD_NONBLOCK` is not given, `eventfd_read()` blocks.

`eventfd_write()` raises the event counter. A write blocks when the write operation would raise the counter beyond 264-2.

Example:

```python
import os

# semaphore with start value '1'
fd = os.eventfd(1, os.EFD_SEMAPHORE | os.EFD_CLOEXEC)
try:
    # acquire semaphore
    v = os.eventfd_read(fd)
    try:
        do_work()
    finally:
        # release semaphore
        os.eventfd_write(fd, v)
finally:
    os.close(fd)

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](os-fwalk-to-os-memfd-create.md) · [Continue](os-eventfd-read-to-os-efd-semaphore.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)

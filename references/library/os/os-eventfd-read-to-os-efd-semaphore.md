# os: `os.eventfd_read()`, `os.eventfd_write()`, `os.EFD_CLOEXEC`, `os.EFD_NONBLOCK`, `os.EFD_SEMAPHORE`

os.eventfd_read(*fd*)

Read a value from an `eventfd()` file descriptor and give back a 64 bit unsigned int. The function does not check that *fd* is an `eventfd()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27

Added in version 3.10.

 os.eventfd_write(*fd*, *value*)

Add value to an `eventfd()` file descriptor. *value* has to be a 64 bit unsigned int. The function does not check that *fd* is an `eventfd()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27

Added in version 3.10.

 os.EFD_CLOEXEC

Set close-on-exec flag for new `eventfd()` file descriptor.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27

Added in version 3.10.

 os.EFD_NONBLOCK

Set `O_NONBLOCK` status flag for new `eventfd()` file descriptor.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27

Added in version 3.10.

 os.EFD_SEMAPHORE

Give reads from an `eventfd()` file descriptor semaphore-like semantics. Each read lowers the internal counter by one.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.30

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](os-mfd-cloexec-to-os-eventfd.md) · [Continue](timerfd-create.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)

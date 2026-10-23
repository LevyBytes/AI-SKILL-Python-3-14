# socket - Timeouts and the `accept` method

### Timeouts and the `accept` method

When `getdefaulttimeout()` is not [`None`](https://docs.python.org/3.14/library/constants.html#None), whatever sockets the `accept()` method hands back take on that timeout. Failing that, the outcome rests on how the listening socket is configured:

- where the listening socket sits in *blocking mode* or in *timeout mode*, the socket `accept()` returns lands in *blocking mode*;

- where the listening socket sits in *non-blocking mode*, whether the socket `accept()` returns ends up blocking or non-blocking is left to the operating system. To lock in cross-platform behaviour, the advice is to override this setting by hand.

[Subject index](INDEX.md) · [Previous](timeouts-and-the-connect-method.md) · [Continue](example-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md)

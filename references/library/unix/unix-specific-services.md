# Unix-specific services

# Unix, Urllib.Error, Urllib

## Overview

Three areas are addressed below: first, the Unix-specific services; next, the `urllib.error` module with its exception classes thrown by `urllib.request`; and finally, the `urllib` package of URL handling modules.

## Unix-specific services

### Unix-specific services

This chapter's modules expose interfaces to capabilities found only on the Unix operating system — or, in certain instances, on some or many of its variants. A summary follows:

- [`shlex` - Simple lexical analysis](https://docs.python.org/3.14/library/shlex.html)
  - [shlex Objects](https://docs.python.org/3.14/library/shlex.html#shlex-objects)
  - [Parsing Rules](https://docs.python.org/3.14/library/shlex.html#parsing-rules)
  - [Improved Compatibility with Shells](https://docs.python.org/3.14/library/shlex.html#improved-compatibility-with-shells)

- [`posix` - The most common POSIX system calls](https://docs.python.org/3.14/library/posix.html)
  - [Large File Support](https://docs.python.org/3.14/library/posix.html#large-file-support)
  - [Notable Module Contents](https://docs.python.org/3.14/library/posix.html#notable-module-contents)

- [`pwd` - The password database](https://docs.python.org/3.14/library/pwd.html)
- [`grp` - The group database](https://docs.python.org/3.14/library/grp.html)
- [`termios` - POSIX style tty control](https://docs.python.org/3.14/library/termios.html)
  - [Example](https://docs.python.org/3.14/library/termios.html#example)

- [`tty` - Terminal control functions](https://docs.python.org/3.14/library/tty.html)
- [`pty` - Pseudo-terminal utilities](https://docs.python.org/3.14/library/pty.html)
  - [Example](https://docs.python.org/3.14/library/pty.html#example)

- [`fcntl` - The `fcntl` and `ioctl` system calls](https://docs.python.org/3.14/library/fcntl.html)
- [`resource` - Resource usage information](https://docs.python.org/3.14/library/resource.html)
  - [Resource Limits](https://docs.python.org/3.14/library/resource.html#resource-limits)
  - [Resource Usage](https://docs.python.org/3.14/library/resource.html#resource-usage)

- [`syslog` - Unix syslog library routines](https://docs.python.org/3.14/library/syslog.html)
  - [Examples](https://docs.python.org/3.14/library/syslog.html#examples)
    - [Simple example](https://docs.python.org/3.14/library/syslog.html#simple-example)

[Subject index](INDEX.md) · [Continue](../urllib-error/urllib-error-urlerror-to-urllib-error-contenttooshorterror.md)

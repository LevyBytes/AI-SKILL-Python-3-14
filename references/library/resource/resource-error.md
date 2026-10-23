# resource`resource` - Resource usage information

# Resource, Rlcompleter

## Overview

Covers: resource — Resource usage information; rlcompleter — Completion function for GNU readline.

## resource - Resource usage information

### `resource` - Resource usage information

---

This module supplies elementary facilities for gauging and regulating the system resources a program consumes.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Named constants serve to pick out individual system resources and to ask for usage figures covering either the running process or its child processes.

When a syscall fails, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised.

 *exception *resource.error

A deprecated alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

Changed in version 3.3: In the wake of [**PEP 3151**](https://peps.python.org/pep-3151/), this class became nothing more than an alias for [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[Subject index](INDEX.md) · [Continue](resource-rlim-infinity-to-resource-rlimit-memlock.md)

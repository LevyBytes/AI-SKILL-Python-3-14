# Unstable C API

### Unstable C API

Whatever API carries the `PyUnstable` prefix surfaces CPython implementation details and is free to change at every minor release (say, 3.9 to 3.10) without any deprecation warnings. That said, it stays fixed across a bugfix release (say, 3.10.0 to 3.10.1).

Its usual audience is specialized, low-level tooling such as debuggers.

Projects relying on this API are expected to track CPython development and put in extra work adapting to changes.

[Subject index](INDEX.md) · [Previous source contract](c-api-stability.md) · [Following source contract](stable-application-binary-interface.md)

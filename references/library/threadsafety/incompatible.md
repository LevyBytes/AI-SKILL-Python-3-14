# Incompatible

### Incompatible

Such a function or operation can never be rendered safe for simultaneous use, not even when callers add their own synchronization. Code marked incompatible usually touches global state without any coordination and should be invoked from one thread alone for the entire run of the program.

Example: a function that alters process-wide state such as signal handlers or environment variables, where simultaneous calls from any threads - even when an external lock is held - can clash with the runtime or with other libraries.

[Subject index](INDEX.md) · [Previous](thread-safety-levels.md) · [Continue](compatible.md)

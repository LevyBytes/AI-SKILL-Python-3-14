# Thread safety

### Thread safety

At the Python layer, the goal of free-threaded CPython is to keep thread-safety roughly matching what you get from the standard GIL-enabled build. Core types such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), and [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) rely on their own internal locks so that simultaneous edits are guarded in a manner reminiscent of the GIL. That said, the language has never formally promised any particular result when these built-in types are mutated concurrently, so read the above as how things work right now rather than a commitment about present or upcoming behavior.

Note

Where you can, lean on [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) or comparable synchronization primitives rather than depending on the built-in types' own internal locks.

[Subject index](INDEX.md) · [Previous source context](the-global-interpreter-lock-in-free-threaded-python.md) · [Following source context](known-limitations.md)

# What Are Critical Sections?

### What Are Critical Sections?

You can picture critical sections as a deadlock-avoidance layer sitting above plain mutexes. Every thread keeps its own stack of the critical sections currently in force. The moment a thread has to take the lock tied to a critical section — whether implicitly, by calling a thread-safe C API routine such as [`PyDict_SetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetItem), or explicitly through the macros — it goes after the mutex beneath it.

[Subject index](INDEX.md) · [Previous source context](critical-sections.md) · [Following source context](using-critical-sections.md)

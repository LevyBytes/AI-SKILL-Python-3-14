# How do I interface to C++ objects from Python?

### How do I interface to C++ objects from Python?

Many routes are open, and the right one hinges on what you need. For the hands-on approach, start by going through [the “Extending and Embedding” document](https://docs.python.org/3.14/extending/index.html#extending-index). Keep in mind that, as far as the Python run-time system is concerned, C and C++ scarcely differ — so the tactic of wrapping a new Python type around a C structure (pointer) type carries over to C++ objects just as well.

When it comes to C++ libraries, refer back to the earlier question on whether alternatives to writing C exist.

[Subject index](INDEX.md)

# Thread Safety Guarantees

# Threadsafety

### Thread Safety Guarantees

This page records the thread-safety promises made for Python's built-in types under the free-threaded build. What follows holds while Python runs with the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) turned off (free-threaded mode). With the GIL active, the bulk of operations are serialized implicitly.

To learn the broader principles of authoring thread-safe code in free-threaded Python, consult [Python support for free threading](https://docs.python.org/3.14/howto/free-threading-python.html#freethreading-python-howto).

[Subject index](INDEX.md) · [Continue](thread-safety-levels.md)

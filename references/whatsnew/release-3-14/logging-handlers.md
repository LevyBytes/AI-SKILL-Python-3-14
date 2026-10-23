# What's new in Python 3.14 / logging.handlers - logging.handlers

### logging.handlers

- The [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol is now honored by [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) objects. (Contributed by Charles Machalow in [gh-132106](https://github.com/python/cpython/issues/132106).)

- Calling [`QueueListener.start`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener.start) now triggers a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) when the listener has already begun. (Contributed by Charles Machalow in [gh-132106](https://github.com/python/cpython/issues/132106).)

[Subject index](INDEX.md) · [Previous source section](linecache.md) · [Next source section](math.md) · [Release/subject declaration](summary-release-highlights.md)

# Can I create an object class with some methods implemented in C and others in Python (e.g. through inheritance)?

### Can I create an object class with some methods implemented in C and others in Python (e.g. through inheritance)?

Yes — subclassing built-in classes is permitted, things like [`int`](https://docs.python.org/3.14/library/functions.html#int), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), and so on.

The Boost Python Library (BPL, [https://www.boost.org/libs/python/doc/index.html](https://www.boost.org/libs/python/doc/index.html)) opens up a way to accomplish this from C++ — through the BPL you can subclass an extension class authored in C++.

[Subject index](INDEX.md)

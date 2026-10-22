# What's new in Python 3.14 / io — io, typing

### io

- When you read text off a non-blocking stream using `read`, a [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError) may now be raised if the call cannot hand back bytes right away. (Contributed by Giovanni Siragusa in [gh-109523](https://github.com/python/cpython/issues/109523).)

- The [`Reader`](https://docs.python.org/3.14/library/io.html#io.Reader) plus [`Writer`](https://docs.python.org/3.14/library/io.html#io.Writer) protocols arrive as easier substitutes for the pseudo-protocols [`typing.IO`](https://docs.python.org/3.14/library/typing.html#typing.IO), [`typing.TextIO`](https://docs.python.org/3.14/library/typing.html#typing.TextIO), and [`typing.BinaryIO`](https://docs.python.org/3.14/library/typing.html#typing.BinaryIO). (Contributed by Sebastian Rittau in [gh-127648](https://github.com/python/cpython/issues/127648).)

### io

- Opening plus reading files now issues fewer system calls. Reading a small operating system cached file fully is as much as 15% faster. (Contributed by Cody Maloney and Victor Stinner in [gh-120754](https://github.com/python/cpython/issues/120754) and [gh-90102](https://github.com/python/cpython/issues/90102).)

[Subject index](INDEX.md) · [Previous source section](inspect.md) · [Next source section](json.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](gc.md) · [Next source section](pathlib.md)

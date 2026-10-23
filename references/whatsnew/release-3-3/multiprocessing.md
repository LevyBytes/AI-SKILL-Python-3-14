# What's New In Python 3.3 / multiprocessing - itertools, multiprocessing, select

### multiprocessing

A new [`multiprocessing.connection.wait()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.wait) function lets you poll several objects at once — connections, sockets, pipes and the like — under a timeout. Richard Oudkerk landed this ([bpo-12328](https://bugs.python.org/issue?@action=redirect&bpo=12328)).

You can now ship [`multiprocessing.connection.Connection`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.Connection) objects across multiprocessing connections. Richard Oudkerk landed this ([bpo-4892](https://bugs.python.org/issue?@action=redirect&bpo=4892)).

A `daemon` keyword argument now reaches [`multiprocessing.Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process), overriding the usual behavior where the `daemon` flag is inherited from the parent process ([bpo-6064](https://bugs.python.org/issue?@action=redirect&bpo=6064)).

The new [`multiprocessing.Process.sentinel`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.sentinel) attribute lets a program block on several [`Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process) objects together by way of the right OS primitives (say, [`select`](https://docs.python.org/3.14/library/select.html#module-select) on posix systems).

Two new methods, [`multiprocessing.pool.Pool.starmap()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.starmap) and [`starmap_async()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.starmap_async), deliver [`itertools.starmap()`](https://docs.python.org/3.14/library/itertools.html#itertools.starmap) counterparts to the existing [`multiprocessing.pool.Pool.map()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.map) and [`map_async()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool.map_async) functions. Hynek Schlawack landed this ([bpo-12708](https://bugs.python.org/issue?@action=redirect&bpo=12708)).

### nntplib

[Subject index](INDEX.md) · [Previous source section](mmap.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](nntplib.md)

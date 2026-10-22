# What's New In Python 3.10 / os — os

### os

Add [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count) support for VxWorks RTOS. (Contributed by Peixing Xin in [bpo-41440](https://bugs.python.org/issue?@action=redirect&bpo=41440).)

Add a new function [`os.eventfd()`](https://docs.python.org/3.14/library/os.html#os.eventfd) plus companion helpers that wrap the Linux `eventfd2` syscall. (Contributed by Christian Heimes in [bpo-41001](https://bugs.python.org/issue?@action=redirect&bpo=41001).)

Add [`os.splice()`](https://docs.python.org/3.14/library/os.html#os.splice), letting you move data across a pair of file descriptors with no copy made between user address space and kernel address space, so long as one of those descriptors refers to a pipe. (Contributed by Pablo Galindo in [bpo-41625](https://bugs.python.org/issue?@action=redirect&bpo=41625).)

Add [`O_EVTONLY`](https://docs.python.org/3.14/library/os.html#os.O_EVTONLY), [`O_FSYNC`](https://docs.python.org/3.14/library/os.html#os.O_FSYNC), [`O_SYMLINK`](https://docs.python.org/3.14/library/os.html#os.O_SYMLINK) and [`O_NOFOLLOW_ANY`](https://docs.python.org/3.14/library/os.html#os.O_NOFOLLOW_ANY) for macOS. (Contributed by Donghee Na in [bpo-43106](https://bugs.python.org/issue?@action=redirect&bpo=43106).)

[Subject index](INDEX.md) · [Previous source section](linecache.md) · [Next source section](os-path.md) · [Release/subject declaration](summary-release-highlights.md)

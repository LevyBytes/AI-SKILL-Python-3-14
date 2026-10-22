# -X cpu_count=*n*

- `-X cpu_count=*n*` supersedes [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count), [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count), and [`multiprocessing.cpu_count()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.cpu_count). *n* has to be at least 1. This option can help users who need to cap the CPU resources of a container system. See also `PYTHON_CPU_COUNT`. When *n* is `default`, nothing is superseded.

Added in version 3.13.

-

[Subject index](INDEX.md) · [Previous source section](x-disable-remote-debug.md)

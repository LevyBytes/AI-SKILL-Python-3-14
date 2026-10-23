# What's New In Python 3.2 / os - os

### os

Filenames and environment variables get encoded differently depending on the operating system. To handle this, the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module gains a pair of functions, [`fsencode()`](https://docs.python.org/3.14/library/os.html#os.fsencode) and [`fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode), that encode and decode filenames:

```python
>>> import os
>>> filename = 'Sehenswürdigkeiten'
>>> os.fsencode(filename)
b'Sehensw\xc3\xbcrdigkeiten'

```

Certain operating systems permit reading the environment as raw encoded bytes. Where that holds, the [`os.supports_bytes_environ`](https://docs.python.org/3.14/library/os.html#os.supports_bytes_environ) constant evaluates to true.

When encoded environment variables are reachable directly, reach for the new [`os.getenvb()`](https://docs.python.org/3.14/library/os.html#os.getenvb) function, or turn to [`os.environb`](https://docs.python.org/3.14/library/os.html#os.environb), the bytes counterpart of [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ).

(Contributed by Victor Stinner.)

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](shutil.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

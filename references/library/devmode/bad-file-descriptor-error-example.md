# Bad file descriptor error example

### Bad file descriptor error example

A script that prints its own opening line:

```python
import os

def main():
    fp = open(__file__)
    firstline = fp.readline()
    print(firstline.rstrip())
    os.close(fp.fileno())
    # The file is closed implicitly

main()

```

Out of the box, Python raises no warning whatsoever:

```shell
$ python script.py
import os

```

The Python Development Mode surfaces a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) and records a “Bad file descriptor” error as the file object is finalized:

```shell
$ python -X dev script.py
import os
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
  main()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
Exception ignored in: <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    main()
OSError: [Errno 9] Bad file descriptor

```

The descriptor is shut by `os.close(fp.fileno())`. Later, when the file object’s finalizer attempts to shut that same descriptor once more, it stumbles into the `Bad file descriptor` error. A descriptor ought to be closed a single time only. At its worst, shutting it twice can trigger a crash (see [bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748) for an instance).

To fix it, drop the `os.close(fp.fileno())` line, or open the file passing `closefd=False`.

[Subject index](INDEX.md) · [Previous](resourcewarning-example.md) · [Continue](../dialog/float-integer-and-string-input-dialogs.md)

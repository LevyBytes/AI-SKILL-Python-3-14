# What’s New In Python 3.5 / subprocess - subprocess

### subprocess

The new [`run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) function is now available. It executes whatever command you give it and yields a [`CompletedProcess`](https://docs.python.org/3.14/library/subprocess.html#subprocess.CompletedProcess) object that captures a process once it has finished. This more uniform API is the suggested way to launch subprocesses from Python code that has no requirement to stay compatible with older Python releases. Thomas Kluyver contributed this (see [bpo-23342](https://bugs.python.org/issue?@action=redirect&bpo=23342)).

Examples:

```python
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')

```

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](sys.md) · [Release/subject declaration](summary-release-highlights.md)

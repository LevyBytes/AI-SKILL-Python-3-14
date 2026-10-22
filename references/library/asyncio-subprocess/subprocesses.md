# Subprocesses

# Asyncio Subprocess

### Subprocesses

**Source code:** [Lib/asyncio/subprocess.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/subprocess.py), [Lib/asyncio/base_subprocess.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/base_subprocess.py)

---

What follows covers the high-level async/await asyncio APIs for spawning and managing subprocesses.

Below is a demonstration of asyncio executing a shell command and capturing what it produces:

```python
import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))

```

will print:

```python
['ls /zzz' exited with 1]
[stderr]
ls: /zzz: No such file or directory

```

Since every asyncio subprocess function is asynchronous and asyncio supplies plenty of facilities for working with such functions, launching and observing several subprocesses concurrently is straightforward. Reworking the example above to fire off multiple commands at the same time is genuinely simple:

```python
async def main():
    await asyncio.gather(
        run('ls /zzz'),
        run('sleep 1; echo "hello"'))

asyncio.run(main())

```

See also the Examples subsection.

[Subject index](INDEX.md) · [Continue](subprocess-exec-and-shell-creation.md)

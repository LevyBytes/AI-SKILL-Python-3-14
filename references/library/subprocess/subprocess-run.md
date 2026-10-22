# subprocess: `subprocess.run()`

### Using the `subprocess` Module

For launching subprocesses, the preferred path is the `run()` function, which covers every scenario it is capable of handling. When you need finer control, reach for the lower-level `Popen` interface on its own.

`subprocess.run(*args*, ***, *stdin=None*, *input=None*, *stdout=None*, *stderr=None*, *capture_output=False*, *shell=False*, *cwd=None*, *timeout=None*, *check=False*, *encoding=None*, *errors=None*, *text=None*, *env=None*, *universal_newlines=None*, ***other_popen_kwargs*)`

Execute the command given by *args*. Block until that command finishes, and then hand back a `CompletedProcess` instance.

What you see above are simply the arguments people reach for most often, which is why the condensed signature marks them keyword-only; they are documented later under Frequently Used Arguments. Apart from that, the complete signature matches the `Popen` constructor almost exactly — the majority of these arguments are forwarded straight to that interface. (The exceptions are *timeout*, *input*, *check*, and *capture_output*.)

When *capture_output* is true, both stdout and stderr get captured. The underlying `Popen` object is then built automatically with *stdout* and *stderr* each set to `PIPE`. You cannot pass the *stdout* and *stderr* arguments together with *capture_output*. To capture both streams merged into a single one, point *stdout* at `PIPE` and *stderr* at `STDOUT` rather than relying on *capture_output*.

You can give a *timeout* in seconds; internally it gets handed off to `Popen.communicate()`. Should that timeout elapse, the child process is killed and then waited on. Once the child has finished, the `TimeoutExpired` exception is re-raised. Because many platform APIs cannot interrupt the act of creating the process itself, a timeout exception is not guaranteed to surface until process creation has taken however long it takes.

The *input* argument flows into `Popen.communicate()` and from there into the subprocess’s stdin. If you supply it, it has to be a byte sequence — or a string when *encoding* or *errors* is given or when *text* is true. Used this way, the underlying `Popen` object is built automatically with *stdin* set to `PIPE`, and you may not pass the *stdin* argument too.

When *check* is true and the process finishes with a non-zero exit code, a `CalledProcessError` exception gets raised. The attributes of that exception carry the arguments, the exit code, plus stdout and stderr when those were captured.

When *encoding* or *errors* is given, or when *text* is true, the file objects for stdin, stdout and stderr open in text mode, using the given *encoding* and *errors* or else the [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) default. The *universal_newlines* argument means the same thing as *text* and exists for backwards compatibility. Otherwise, file objects open in binary mode by default.

When *env* is not `None`, it has to be a mapping defining the environment variables for the new process; these take the place of the usual behavior of inheriting the environment of the current process. It goes straight through to `Popen`. On any platform the mapping is allowed to be str keyed to str, while on POSIX platforms bytes keyed to bytes also works, in the same fashion as [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) or [`os.environb`](https://docs.python.org/3.14/library/os.html#os.environb).

Examples:

```python
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')

```

Added in version 3.5.

Changed in version 3.6: Added *encoding* and *errors* parameters

Changed in version 3.7: The *text* parameter arrived, serving as a clearer alias for *universal_newlines*. The *capture_output* parameter was also introduced.

Changed in version 3.12: On Windows the lookup order for the shell under `shell=True` was revised. In place of the current directory and `%PATH%`, it now uses `%COMSPEC%` together with `%SystemRoot%\System32\cmd.exe`. Consequently, planting a hostile binary called `cmd.exe` in a current directory is no longer effective.

[Subject index](INDEX.md) · [Previous](subprocess-subprocess-management.md) · [Continue](completed-process-result-and-return-code.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

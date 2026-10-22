# subprocess: `subprocess.call()`, `subprocess.check_call()`

### Older high-level API

Before Python 3.5 arrived, these three functions made up the high level API to subprocess. While `run()` now covers many situations, a great deal of existing code still calls these functions.

 `subprocess.call(*args, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)`

Execute whatever command *args* describes. Hold until the command finishes, then hand back the `returncode` attribute.

When your code has to capture stdout or stderr, reach for `run()` in its place:

```python
run(...).returncode

```

Pass a value of `DEVNULL` to silence stdout or stderr.

Only a handful of the more usual arguments appear above. This function's complete signature matches the `Popen` constructor's, and every argument you give it apart from *timeout* is handed straight through to that interface.

Note

Steer clear of `stdout=PIPE` or `stderr=PIPE` alongside this function. Because nothing reads the pipes, the child process stalls once its output grows large enough to saturate the OS pipe buffer.

Changed in version 3.3: *timeout* was added.

Changed in version 3.12: The Windows shell search order for `shell=True` was revised. In place of the current directory and `%PATH%`, the lookup now uses `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. Consequently, planting a hostile program called `cmd.exe` in a current directory has stopped being effective.

 `subprocess.check_call(*args, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)`

Execute the command together with its arguments. Hold until the command finishes. Return when the return code came back zero; otherwise raise `CalledProcessError`. That `CalledProcessError` object carries the return code inside its `returncode` attribute. Should `check_call()` fail to launch the process, it forwards whatever exception was raised.

When your code has to capture stdout or stderr, reach for `run()` in its place:

```python
run(..., check=True)

```

Pass a value of `DEVNULL` to silence stdout or stderr.

Only a handful of the more usual arguments appear above. This function's complete signature matches the `Popen` constructor's, and every argument you give it apart from *timeout* is handed straight through to that interface.

Note

Steer clear of `stdout=PIPE` or `stderr=PIPE` alongside this function. Because nothing reads the pipes, the child process stalls once its output grows large enough to saturate the OS pipe buffer.

Changed in version 3.3: *timeout* was added.

[Subject index](INDEX.md) · [Previous](windows-process-priority-and-job-flags.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Required continuation of the source contract](subprocess-check-output.md)

# subprocess: Popen creation flags and stream-buffer configuration

`BELOW_NORMAL_PRIORITY_CLASS`

- `HIGH_PRIORITY_CLASS`

- `IDLE_PRIORITY_CLASS`

- `NORMAL_PRIORITY_CLASS`

- `REALTIME_PRIORITY_CLASS`

- `CREATE_NO_WINDOW`

- `DETACHED_PROCESS`

- `CREATE_DEFAULT_ERROR_MODE`

- `CREATE_BREAKAWAY_FROM_JOB`

You can supply *pipesize* to adjust the pipe's size whenever `PIPE` is used for *stdin*, *stdout* or *stderr*. The pipe's size is adjusted solely on platforms that allow it (just Linux as of this writing). The remaining platforms disregard this parameter.

Changed in version 3.10: Added the *pipesize* parameter.

Popen objects work as context managers through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement: when the block exits, the standard file descriptors are closed and the process is awaited.

```python
with Popen(["ifconfig"], stdout=PIPE) as proc:
    log.write(proc.stdout.read())

```

Both Popen and every other function in this module that relies on it raise an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `subprocess.Popen` carrying the arguments `executable`, `args`, `cwd`, and `env`. Depending on the platform, the `args` value may be one string or a list of strings.

Changed in version 3.2: Added context manager support.

Changed in version 3.6: should the child process still be running, the Popen destructor now raises a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) warning.

Changed in version 3.8: for a performance boost, Popen may turn to [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) under certain conditions. Across Windows Subsystem for Linux and QEMU User Emulation, a Popen constructor relying on `os.posix_spawn()` will no longer throw an exception for faults such as an absent program; instead the child process ends with a non-zero `returncode`.

[Subject index](INDEX.md) · [Previous](popen-working-directory-and-platform-options.md) · [Continue](exceptions.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: subprocess.Popen](subprocess-popen-class.md) · [Owning module, declaration or section: Popen Constructor](popen-constructor.md)

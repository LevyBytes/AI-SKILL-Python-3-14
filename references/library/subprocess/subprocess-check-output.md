# subprocess: `subprocess.check_output()`

Changed in version 3.12: The Windows shell search order under `shell=True` was reworked. In place of the current directory and `%PATH%`, the lookup now uses `%COMSPEC%` together with `%SystemRoot%\System32\cmd.exe`. Because of that, planting a hostile program called `cmd.exe` inside a current directory no longer has any effect.

 `subprocess.check_output(*args*, ***, *stdin=None*, *stderr=None*, *shell=False*, *cwd=None*, *encoding=None*, *errors=None*, *universal_newlines=None*, *timeout=None*, *text=None*, ***other_popen_kwargs*)`

Execute the command along with its arguments and hand back what it prints.

A non-zero return code makes it raise a `CalledProcessError`. That `CalledProcessError` object keeps the return code on its `returncode` attribute and whatever was produced on its `output` attribute.

That amounts to:

```python
run(..., check=True, stdout=PIPE).stdout

```

What you see above is only a selection of the more common arguments. By and large the complete function signature lines up with that of `run()`, and most arguments are handed straight through to that interface. There is a single API difference from how `run()` behaves: supplying `input=None` acts just like `input=b''` (or `input=''`, depending on the other arguments) instead of drawing on the parent’s standard input file handle.

Out of the box, the function gives the data back as encoded bytes. Since the real encoding of that output can hinge on whichever command you ran, turning it into text frequently has to be taken care of by your application itself.

You can override that behaviour by giving *text*, *encoding*, *errors*, or *universal_newlines* the value `True`, as covered under Frequently Used Arguments and `run()`.

If you want standard error folded into the result as well, pass `stderr=subprocess.STDOUT`:

```python
>>> subprocess.check_output(
...     "ls non_existent_file; exit 0",
...     stderr=subprocess.STDOUT,
...     shell=True)
'ls: non_existent_file: No such file or directory\n'

```

Added in version 3.1.

Changed in version 3.3: The *timeout* argument was introduced.

Changed in version 3.4: The *input* keyword argument gained support.

Changed in version 3.6: The *encoding* and *errors* arguments were introduced. Consult `run()` for the specifics.

Added in version 3.7: *text* arrived as an easier-to-read alias standing in for *universal_newlines*.

Changed in version 3.12: On Windows, the shell search order for `shell=True` was altered. The lookup swaps the current directory and `%PATH%` out for `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. The upshot is that slipping a malicious program named `cmd.exe` into a current directory ceases to accomplish anything.

[Subject index](INDEX.md) · [Continue](replacing-older-functions-with-the-subprocess-module.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: Older high-level API](subprocess-call-to-subprocess-check-call.md) · [Owning module, declaration or section: subprocess.check_call](subprocess-call-to-subprocess-check-call.md) · [Preceding source contract and version conditions](subprocess-call-to-subprocess-check-call.md)

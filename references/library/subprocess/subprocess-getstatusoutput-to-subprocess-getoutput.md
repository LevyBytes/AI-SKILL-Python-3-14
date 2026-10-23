# subprocess - Legacy Shell Invocation Functions

### Legacy Shell Invocation Functions

This module additionally carries over the legacy functions listed below from the 2.x `commands` module. Each of these operations silently calls out to the system shell, and not one of the security and exception-handling-consistency guarantees laid out earlier holds for them.

 subprocess.getstatusoutput(*cmd*, ***, *encoding=None*, *errors=None*)

Hand back the `(exitcode, output)` from running *cmd* within a shell.

Run the string *cmd* inside a shell by way of `check_output()`, then give back a 2-tuple `(exitcode, output)`. The *encoding* and *errors* values govern how the output is decoded; the notes under Frequently Used Arguments spell this out further.

Any newline at the very end of the output is removed. You can read the command’s exit code as the subprocess return code. Example:

```python
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')
>>> subprocess.getstatusoutput('cat /bin/junk')
(1, 'cat: /bin/junk: No such file or directory')
>>> subprocess.getstatusoutput('/bin/junk')
(127, 'sh: /bin/junk: not found')
>>> subprocess.getstatusoutput('/bin/kill $$')
(-15, '')

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.3.4: Support for Windows was introduced.

Where Python 3.3.3 and earlier had the function return (status, output), it now returns (exitcode, output) instead. The exitcode carries the very same value as `returncode`.

Changed in version 3.11: The *encoding* and *errors* parameters were introduced.

 subprocess.getoutput(*cmd*, ***, *encoding=None*, *errors=None*)

Hand back the output (both stdout and stderr) from running *cmd* within a shell.

Behaves like `getstatusoutput()`, save that the exit code is disregarded and the value handed back is simply a string holding the command’s output. Example:

```python
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.3.4: Windows became supported

Changed in version 3.11: The *encoding* and *errors* parameters were brought in.

[Subject index](INDEX.md) · [Previous](replacing-os-popen.md) · [Continue](timeout-behavior.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

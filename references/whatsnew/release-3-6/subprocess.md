# What's New In Python 3.6 / subprocess — subprocess

### subprocess

When the child is still alive, the [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) destructor now raises a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) warning. To collect the child process's exit status, apply the context manager protocol (`with proc: ...`) or call the [`wait()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.wait) method directly. (Contributed by Victor Stinner in [bpo-26741](https://bugs.python.org/issue?@action=redirect&bpo=26741).)

Both the [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) constructor and every function forwarding arguments to it now take *encoding* and *errors* arguments. Supplying either one switches the *stdin*, *stdout* and *stderr* streams into text mode. (Contributed by Steve Dower in [bpo-6135](https://bugs.python.org/issue?@action=redirect&bpo=6135).)

[Subject index](INDEX.md) · [Previous source section](struct.md) · [Next source section](sys.md) · [Release/subject declaration](summary-release-highlights.md)

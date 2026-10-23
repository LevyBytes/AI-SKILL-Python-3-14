# What's New In Python 3.7 / subprocess - subprocess

### subprocess

The [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) function takes a new *capture_output* keyword argument. Set it true and both stdout and stderr get captured, which amounts to handing [`subprocess.PIPE`](https://docs.python.org/3.14/library/subprocess.html#subprocess.PIPE) along as the *stdout* and *stderr* arguments. (Contributed by Bo Bayles in [bpo-32102](https://bugs.python.org/issue?@action=redirect&bpo=32102).)

Both the `subprocess.run` function and the [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) constructor will now take the *text* keyword argument as another name for *universal_newlines*. (Contributed by Andrew Clegg in [bpo-31756](https://bugs.python.org/issue?@action=redirect&bpo=31756).)

On Windows, while redirecting the standard handles, the *close_fds* default flipped from `False` to `True`. You can now set *close_fds* to true even as the standard handles are redirected. See [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen). The upshot is that *close_fds* now defaults to `True` on every supported platform. (Contributed by Segev Finer in [bpo-19764](https://bugs.python.org/issue?@action=redirect&bpo=19764).)

When [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) arrives during [`subprocess.call()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.call), [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run), or inside a [`Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) context manager, the subprocess module now copes more gracefully. Before it resumes propagating the `KeyboardInterrupt` exception, it briefly pauses to give the child a chance to exit. (Contributed by Gregory P. Smith in [bpo-25942](https://bugs.python.org/issue?@action=redirect&bpo=25942).)

[Subject index](INDEX.md) · [Previous source section](string.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](sys.md)

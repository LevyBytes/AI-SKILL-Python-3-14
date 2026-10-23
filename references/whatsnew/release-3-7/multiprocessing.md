# What's New In Python 3.7 / multiprocessing - multiprocessing, signal

### multiprocessing

A new [`Process.close()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.close) method deliberately closes the process object and frees every resource tied to it. A [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised should the underlying process still be running. (Contributed by Antoine Pitrou in [bpo-30596](https://bugs.python.org/issue?@action=redirect&bpo=30596).)

A new [`Process.kill()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.kill) method lets you end the process by sending the [`SIGKILL`](https://docs.python.org/3.14/library/signal.html#signal.SIGKILL) signal on Unix. (Contributed by Vitor Pereira in [bpo-30794](https://bugs.python.org/issue?@action=redirect&bpo=30794).)

When a [`Process`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process) creates non-daemonic threads, those threads are now joined as the process exits. (Contributed by Antoine Pitrou in [bpo-18966](https://bugs.python.org/issue?@action=redirect&bpo=18966).)

[Subject index](INDEX.md) · [Previous source section](msilib.md) · [Next source section](os.md) · [Release/subject declaration](summary-release-highlights.md)

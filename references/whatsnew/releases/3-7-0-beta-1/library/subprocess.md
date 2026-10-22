# Python 3.7.0 beta 1 / library / subprocess

[bpo-25942](https://bugs.python.org/issue?@action=redirect&bpo=25942): Handling of a Ctrl-C KeyboardInterrupt that arrives during subprocess.call, subprocess.run, or a Popen context manager is now gentler in the subprocess module. Before resuming the KeyboardInterrupt exception handling, it pauses briefly so the child — which is assumed to have received the SIGINT too — gets a chance to exit. A SIGKILL is still issued by the call() and run() APIs, yet the child at least had its opportunity beforehand.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

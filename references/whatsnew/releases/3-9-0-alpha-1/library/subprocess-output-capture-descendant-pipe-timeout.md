# Python 3.9.0 alpha 1 / library / cleared hang could occur timeout applied subprocess run during output

[bpo-37424](https://bugs.python.org/issue?@action=redirect&bpo=37424): Cleared a hang that could occur when a timeout is applied to `subprocess.run()` during output capture. Should the child process have launched children of its own, or otherwise tied its stdout or stderr handles to a separate process, we might hang once the timeout elapsed and our child was terminated as we tried to read the final output off the pipes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 alpha 3 / library / subprocess

[bpo-38630](https://bugs.python.org/issue?@action=redirect&bpo=38630): Under Unix, [`subprocess.Popen.send_signal()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.send_signal) now checks the process status by polling. That polling cuts the chance of signaling the wrong process when the process has finished, the [`subprocess.Popen.returncode`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.returncode) attribute remains `None`, and the pid was recycled onto some other process.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

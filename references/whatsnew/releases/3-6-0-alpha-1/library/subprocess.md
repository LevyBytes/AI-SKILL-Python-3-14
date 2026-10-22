# Python 3.6.0 alpha 1 / library / subprocess

[bpo-25764](https://bugs.python.org/issue?@action=redirect&bpo=25764): Within the subprocess module, any exception triggered by a fork() failure is now kept intact whenever preexec_fn has been supplied.

[bpo-22274](https://bugs.python.org/issue?@action=redirect&bpo=22274): Within the subprocess module, stderr may now be sent to stdout even in cases where stdout itself has not been redirected. Akira Li wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

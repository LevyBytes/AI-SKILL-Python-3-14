# Python 3.11.0 alpha 7 / library / subprocess

[bpo-47151](https://bugs.python.org/issue?@action=redirect&bpo=47151): Should an attempt at vfork return an error, subprocess now reverts to fork. That makes it usable wherever the OS kernel forbids vfork.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

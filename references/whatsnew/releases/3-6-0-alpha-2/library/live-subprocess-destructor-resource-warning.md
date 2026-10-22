# Python 3.6.0 alpha 2 / library / subprocess popen destructor raises resourcewarning whenever child process still alive

[bpo-26741](https://bugs.python.org/issue?@action=redirect&bpo=26741): The subprocess.Popen destructor now raises a ResourceWarning whenever the child process is still alive.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

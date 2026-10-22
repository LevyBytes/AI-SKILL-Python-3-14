# Python 3.8.0 alpha 4 / macos / resource

[bpo-34602](https://bugs.python.org/issue?@action=redirect&bpo=34602): Sidestep the failures that arose when setting the macOS stack resource limit through resource.setrlimit. This rolls back a previous fix for [bpo-18075](https://bugs.python.org/issue?@action=redirect&bpo=18075), which had imposed a non-default stack size while compiling the interpreter executable on macOS.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.8.0 alpha 1 / library / subprocess

[bpo-32777](https://bugs.python.org/issue?@action=redirect&bpo=32777): Resolve an uncommon yet possible deadlock during the pre-exec stage of a subprocess child on POSIX, occurring while flagging file descriptors as inheritable across exec from the child. The defect seems to trace back to 3.4.

[bpo-8110](https://bugs.python.org/issue?@action=redirect&bpo=8110): [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) was refactored to test for Windows-specific modules instead of checking `sys.platform == 'win32'`.

[bpo-35537](https://bugs.python.org/issue?@action=redirect&bpo=35537): The [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module may now invoke the [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) function under certain circumstances to gain performance.

[bpo-32844](https://bugs.python.org/issue?@action=redirect&bpo=32844): Repair the incorrect redirection of a low descriptor (0 or 1) to stderr in subprocess whenever another low descriptor is closed.

[bpo-34658](https://bugs.python.org/issue?@action=redirect&bpo=34658): Fixed an uncommon SystemError interpreter unhandled-exception state observed only when subprocess runs with a preexec_fn while an after_parent handler is registered through os.register_at_fork and the fork system call then fails.

[bpo-32490](https://bugs.python.org/issue?@action=redirect&bpo=32490): Stopped filenames from being duplicated within [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) exception messages. Zackery Spytz wrote the patch.

[bpo-32270](https://bugs.python.org/issue?@action=redirect&bpo=32270): The subprocess module no longer wrongly closes redirected fds when those fds were listed in pass_fds outside of the default {0, 1, 2} set.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

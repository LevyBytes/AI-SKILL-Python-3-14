# Python 3.5.0 alpha 1 / library / subprocess

[bpo-21618](https://bugs.python.org/issue?@action=redirect&bpo=21618): The subprocess module sometimes failed to shut open fds inherited from the calling process that already sat above POSIX resource limits. Where a working /proc/self/fd or /dev/fd interface exists the cap is now disregarded and every fd is closed.

[bpo-21291](https://bugs.python.org/issue?@action=redirect&bpo=21291): Popen.wait() in subprocess is now thread safe, letting several threads invoke wait() or poll() against one Popen instance concurrently and still keep the Popen.returncode value intact.

[bpo-22182](https://bugs.python.org/issue?@action=redirect&bpo=22182): Within distutils.file_util.move_file, exceptions are now unpacked correctly through e.args. Claudiu Popa wrote the patch.

- The webbrowser module has switched to subprocess's start_new_session=True in place of the comparatively dangerous preexec_fn=os.setsid invocation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.0 alpha 3 / library / files and paths

[bpo-23252](https://bugs.python.org/issue?@action=redirect&bpo=23252): Writing ZIP files onto unseekable streams is now supported.

[bpo-22181](https://bugs.python.org/issue?@action=redirect&bpo=22181): Under Linux, os.urandom() now draws on the new getrandom() syscall where present, a syscall added to the Linux kernel at version 3.17. It proves more dependable and more secure, since it removes the need for a file descriptor and waits for the kernel to gather enough entropy.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

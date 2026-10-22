# Python 3.6.1 release candidate 1 / library / tests and documentation

[bpo-28624](https://bugs.python.org/issue?@action=redirect&bpo=28624): Add a test confirming that the cwd parameter of Popen() takes PathLike objects. Sayan Chowdhury wrote the patch.

[bpo-29335](https://bugs.python.org/issue?@action=redirect&bpo=29335): Repair subprocess.Popen.wait() whenever the child process has exited into a stopped rather than terminated state (for example, while under ptrace).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

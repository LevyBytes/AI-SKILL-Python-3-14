# Python 3.5.4 release candidate 1 / library / correct subprocess popen wait case where child moved into stopped rather

[bpo-29335](https://bugs.python.org/issue?@action=redirect&bpo=29335): Correct subprocess.Popen.wait() for the case where the child has moved into a stopped rather than terminated state (for instance, while under ptrace).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

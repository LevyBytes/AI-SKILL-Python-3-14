# Python 3.7.0 alpha 1 / library / subprocess popen wait corrected case where child entered stopped state instead

[bpo-29335](https://bugs.python.org/issue?@action=redirect&bpo=29335): subprocess.Popen.wait() was corrected for the case where the child has entered a stopped state instead of a terminated one (for instance while under ptrace).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.5.0 alpha 1 / library / ensure bufsize subprocess popen selects line buffering rather than block

[bpo-21332](https://bugs.python.org/issue?@action=redirect&bpo=21332): Ensure that `bufsize=1` in subprocess.Popen() selects line buffering, rather than block buffering. Akira Li supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

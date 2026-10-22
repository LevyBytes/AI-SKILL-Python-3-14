# Python 3.10.0 alpha 3 / library / termios

[bpo-41818](https://bugs.python.org/issue?@action=redirect&bpo=41818): Refreshed the tests covering the pty library. test_basic() was renamed to test_openpty(); it now additionally verifies that slave termios and slave winsize get set correctly by pty.openpty(). To extend coverage to FreeBSD, NetBSD, OpenBSD, and Darwin, a new test_master_read() is also added, showing that pty.spawn() ought not lean on an OSError to break out of its copy loop.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

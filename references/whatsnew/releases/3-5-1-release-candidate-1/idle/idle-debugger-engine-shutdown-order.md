# Python 3.5.1 release candidate 1 / idle / halt debugger engine usually lives user process before debugger

[bpo-15348](https://bugs.python.org/issue?@action=redirect&bpo=15348): Halt the debugger engine — which usually lives in a user process — before the debugger window (hosted in the IDLE process) is closed. Doing so heads off the RuntimeErrors that previously got swallowed silently.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

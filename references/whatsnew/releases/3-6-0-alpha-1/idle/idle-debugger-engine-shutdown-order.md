# Python 3.6.0 alpha 1 / idle / debugger engine normally runs user process halted ahead closing

[bpo-15348](https://bugs.python.org/issue?@action=redirect&bpo=15348): The debugger engine (which normally runs in a user process) is now halted ahead of closing the debugger window (which runs inside the IDLE process). This keeps the RuntimeErrors — formerly caught and silently ignored — from occurring.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

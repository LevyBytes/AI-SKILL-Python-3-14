# Python 3.11.0 alpha 6 / build / subprocess

[bpo-40280](https://bugs.python.org/issue?@action=redirect&bpo=40280): Settle wasm32-emscripten test failures plus platform issues. - Turn off syscalls that go unsupported or misbehave, e.g. wait, getrusage, prlimit, mkfifo, mknod, setres[gu]id, setgroups. - Lean on fd_count to tally open fds. - Layer in more checks around subprocess and fork. - Provide workarounds for the missing _multiprocessing and a failing socket.accept(). - Switch on bzip2. - Switch off large file support. - Switch off signal.alarm.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

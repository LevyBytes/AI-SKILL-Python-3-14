# Python 3.6.0 alpha 2 / tests / files and paths

[bpo-25285](https://bugs.python.org/issue?@action=redirect&bpo=25285): Passing the -j1 command line option to regrtest now spins up subprocesses, so each test file runs inside its own fresh child process. Previously the -j1 option had simply been ignored.

[bpo-25285](https://bugs.python.org/issue?@action=redirect&bpo=25285): By default the Tools/buildbot/test.bat script now passes -j1, letting every test file run in a fresh child process.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

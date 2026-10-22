# Python 3.9.0 alpha 3 / library / functions and types

[bpo-35182](https://bugs.python.org/issue?@action=redirect&bpo=35182): A crash on a follow-up `Popen.communicate()` call was fixed for the situation where the child process has already closed a piped standard stream yet keeps running. Andriy Maletsky wrote the patch.

[bpo-38473](https://bugs.python.org/issue?@action=redirect&bpo=38473): Autospecced methods attached through `unittest.mock.attach_mock()` now take their signature from the inner mock. Karthikeyan Singaravelan wrote the patch.

[bpo-37958](https://bugs.python.org/issue?@action=redirect&bpo=37958): The pstats.Stats.get_profile_dict() method was added, returning the profile data wrapped in a StatsProfile instance.

[bpo-39366](https://bugs.python.org/issue?@action=redirect&bpo=39366): The `xpath()` and `xgtitle()` methods of `nntplib.NNTP`, deprecated earlier, were removed.

[bpo-39313](https://bugs.python.org/issue?@action=redirect&bpo=39313): A fresh `exec_function` option (*–exec-function* on the CLI) was added to `RefactoringTool` so that `exec` becomes a function. Batuhan Taskaya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

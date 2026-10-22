# Python 3.6.1 release candidate 1 / library / functions and types

[bpo-29271](https://bugs.python.org/issue?@action=redirect&bpo=29271): Repair Task.current_task and Task.all_tasks, implemented in C, so they accept a None argument just as their pure Python implementation does.

[bpo-29444](https://bugs.python.org/issue?@action=redirect&bpo=29444): Corrected the out-of-bounds buffer access within the group() method of the match object. WGH's patch served as the basis.

[bpo-28961](https://bugs.python.org/issue?@action=redirect&bpo=28961): Repair the unittest.mock._Call helper: the name parameter is no longer disregarded. Jiajun Huang wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

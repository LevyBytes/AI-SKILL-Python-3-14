# Python 3.8.0 alpha 1 / windows / venv

[bpo-35854](https://bugs.python.org/issue?@action=redirect&bpo=35854): Repair EnvBuilder along with –symlinks in venv under Windows.

[bpo-35811](https://bugs.python.org/issue?@action=redirect&bpo=35811): Keep venv settings from carrying over while launching by way of py.exe.

[bpo-34977](https://bugs.python.org/issue?@action=redirect&bpo=34977): venv under Windows will henceforth employ a python.exe redirector instead of duplicating the real binaries out of the base environment.

[bpo-34011](https://bugs.python.org/issue?@action=redirect&bpo=34011): A block of code that duplicated DLLs and init.tcl from the live Python location into a venv under construction was reworked. Those duplicates matter only while running from a Python source build, so the copying code now triggers exclusively in that scenario rather than upon every venv creation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

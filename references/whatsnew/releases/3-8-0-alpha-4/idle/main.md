# Python 3.8.0 alpha 4 / idle / main

[bpo-36429](https://bugs.python.org/issue?@action=redirect&bpo=36429): Repair the launch of IDLE via pyshell. Place an idlelib.pyshell alias near the top and delete the pyshell alias at the bottom. Strip out the outdated __name__=="__main__" command.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

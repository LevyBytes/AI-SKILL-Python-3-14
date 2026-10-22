# Python 3.6.5 release candidate 1 / windows / memory and lifetimes

[bpo-33016](https://bugs.python.org/issue?@action=redirect&bpo=33016): Repair a possible read of uninitialized memory within nt._getfinalpathname

[bpo-32903](https://bugs.python.org/issue?@action=redirect&bpo=32903): Close a memory leak from os.chdir() on Windows that occurred when the current directory pointed at a UNC path.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

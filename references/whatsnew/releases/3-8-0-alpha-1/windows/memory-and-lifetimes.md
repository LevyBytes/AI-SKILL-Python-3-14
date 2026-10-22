# Python 3.8.0 alpha 1 / windows / memory and lifetimes

[bpo-33016](https://bugs.python.org/issue?@action=redirect&bpo=33016): Repair a possible read of uninitialized memory inside nt._getfinalpathname.

[bpo-32903](https://bugs.python.org/issue?@action=redirect&bpo=32903): Repair a memory leak within os.chdir() under Windows whenever the current directory points at a UNC path.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

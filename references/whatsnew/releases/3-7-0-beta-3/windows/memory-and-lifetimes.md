# Python 3.7.0 beta 3 / windows / memory and lifetimes

[bpo-33016](https://bugs.python.org/issue?@action=redirect&bpo=33016): Address a possible read of uninitialized memory within nt._getfinalpathname

[bpo-32903](https://bugs.python.org/issue?@action=redirect&bpo=32903): Resolve a leak of memory in os.chdir() under Windows whenever the working directory gets pointed at a UNC path.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

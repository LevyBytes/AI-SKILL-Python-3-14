# Python 3.7.0 alpha 1 / build / threads and concurrency

[bpo-31370](https://bugs.python.org/issue?@action=redirect&bpo=31370): Drop the ability to build –without-threads. That option no longer carries much value in the 21st century. Eliminating the many conditional branches lets us streamline the code base, even within the hard-to-maintain low-level internals.

[bpo-30854](https://bugs.python.org/issue?@action=redirect&bpo=30854): Repair the compile failure encountered when building –without-threads. Masayuki Yamamoto supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

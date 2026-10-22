# Python 3.5.3 release candidate 1 / library / multiprocessing

[bpo-28779](https://bugs.python.org/issue?@action=redirect&bpo=28779): multiprocessing.set_forkserver_preload() would take down the forkserver process whenever a preloaded module created some multiprocessing objects such as locks.

[bpo-21201](https://bugs.python.org/issue?@action=redirect&bpo=21201): Makes the multiprocessing error message easier to read. Wojciech Walczak gets the credit for this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

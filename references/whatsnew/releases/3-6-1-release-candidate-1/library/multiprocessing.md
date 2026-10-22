# Python 3.6.1 release candidate 1 / library / multiprocessing

[bpo-29519](https://bugs.python.org/issue?@action=redirect&bpo=29519): Repair weakref spewing exceptions throughout interpreter shutdown whenever it is combined with a rare mix of multiprocessing and custom codecs.

[bpo-28779](https://bugs.python.org/issue?@action=redirect&bpo=28779): multiprocessing.set_forkserver_preload() used to crash the forkserver process whenever a preloaded module created some multiprocessing objects such as locks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

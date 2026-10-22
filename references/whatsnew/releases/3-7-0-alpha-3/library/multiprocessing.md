# Python 3.7.0 alpha 3 / library / multiprocessing

[bpo-31310](https://bugs.python.org/issue?@action=redirect&bpo=31310): the semaphore tracker belonging to multiprocessing ought to be relaunched after a crash.

[bpo-31308](https://bugs.python.org/issue?@action=redirect&bpo=31308): Shield multiprocessing's forkserver process from Ctrl-C along with other user interruptions. Should it crash, bring it back up whenever that is needed.

[bpo-31653](https://bugs.python.org/issue?@action=redirect&bpo=31653): Should a multiprocessing semaphore be acquirable right away, the GIL is no longer released.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

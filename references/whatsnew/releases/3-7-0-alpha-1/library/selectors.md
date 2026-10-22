# Python 3.7.0 alpha 1 / library / selectors

[bpo-27759](https://bugs.python.org/issue?@action=redirect&bpo=27759): Repaired selectors that wrongly held on to invalid file descriptors. Mark Williams authored the patch.

[bpo-30624](https://bugs.python.org/issue?@action=redirect&bpo=30624): Because selectors ignored KeyboardInterrupt and SystemExit, a fd could be left in a bad state on error. Giampaolo Rodola’ contributed the fix.

[bpo-30014](https://bugs.python.org/issue?@action=redirect&bpo=30014): For the poll(), epoll() and devpoll() backed classes within the selectors module, the modify() method runs roughly 10% quicker. Giampaolo Rodola’ contributed it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

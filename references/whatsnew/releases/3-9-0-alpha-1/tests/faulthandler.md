# Python 3.9.0 alpha 1 / tests / faulthandler

[bpo-37531](https://bugs.python.org/issue?@action=redirect&bpo=37531): When a timeout hits, regrtest stops trying to invoke `popen.communicate()` a second time, because it may stall until every child process holding stdout and stderr pipes is done. The worker process is killed and its output discarded. The faulthandler timeout for the main process is also moved from 1 minute up to 5 minutes, to suit Python's slowest buildbots.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

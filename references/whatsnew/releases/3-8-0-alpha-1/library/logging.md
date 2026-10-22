# Python 3.8.0 alpha 1 / library / logging

[bpo-33165](https://bugs.python.org/issue?@action=redirect&bpo=33165): Gave logging calls a stacklevel parameter so wrapper/helper functions can be employed for logging APIs.

[bpo-30805](https://bugs.python.org/issue?@action=redirect&bpo=30805): Sidestepped a race condition involving debug logging

[bpo-34849](https://bugs.python.org/issue?@action=redirect&bpo=34849): The wait on `selector.select` in the asyncio loop iteration is no longer logged. That wait is entirely ordinary for any asyncio program, so logging its duration only clutters the logs with noise and offers nothing useful.

[bpo-6721](https://bugs.python.org/issue?@action=redirect&bpo=6721): During fork()ing, the logging module's frequently used internal locks are now acquired to keep the child process from deadlocking.

[bpo-34630](https://bugs.python.org/issue?@action=redirect&bpo=34630): SSL certificate errors are no longer logged in asyncio code (the connection-error logging is already bypassed).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

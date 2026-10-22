# Python 3.6.4 release candidate 1 / library / memory and lifetimes

[bpo-30058](https://bugs.python.org/issue?@action=redirect&bpo=30058): Corrected a buffer overflow inside select.kqueue.control().

[bpo-31620](https://bugs.python.org/issue?@action=redirect&bpo=31620): An empty asyncio.Queue will no longer leak memory once queue.get pollers reach their timeout

[bpo-31675](https://bugs.python.org/issue?@action=redirect&bpo=31675): Plugged memory leaks in the splitlist() and split() methods of Tkinter whenever a string above 2 GiB is handed over.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

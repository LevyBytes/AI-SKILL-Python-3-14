# Python 3.5.0 alpha 1 / library / threads and concurrency

[bpo-21137](https://bugs.python.org/issue?@action=redirect&bpo=21137): The repr of threading.Lock() and its relatives was improved to display whether it is ?locked? or ?unlocked?. Berker Peksag wrote the patch.

[bpo-11866](https://bugs.python.org/issue?@action=redirect&bpo=11866): The race condition while computing names for new threads was eliminated.

[bpo-22423](https://bugs.python.org/issue?@action=redirect&bpo=22423): An unhandled exception in a thread no longer leads to an unhandled AttributeError when sys.stderr is None.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

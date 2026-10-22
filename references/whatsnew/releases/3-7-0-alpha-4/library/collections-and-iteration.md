# Python 3.7.0 alpha 4 / library / collections and iteration

[bpo-31721](https://bugs.python.org/issue?@action=redirect&bpo=31721): Stop a Python crash from occurring whenever Future._log_traceback gets manually set to True. From now on it may only be set to False, otherwise a ValueError gets raised.

[bpo-32199](https://bugs.python.org/issue?@action=redirect&bpo=32199): The getnode() ip getter now turns to "ip link" rather than "ip link list".

[bpo-27456](https://bugs.python.org/issue?@action=redirect&bpo=27456): Make sure TCP_NODELAY gets set on Linux. Victor Stinner contributed the tests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

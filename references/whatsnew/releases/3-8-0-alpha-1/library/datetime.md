# Python 3.8.0 alpha 1 / library / datetime

[bpo-22005](https://bugs.python.org/issue?@action=redirect&bpo=22005): Added unpickling of [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) instances that Python 2 had pickled. To decode them successfully, use `encoding='latin1'`.

[bpo-34454](https://bugs.python.org/issue?@action=redirect&bpo=34454): Stopped the .fromisoformat() methods of datetime types from crashing when handed unicode containing code points that cannot be encoded as UTF-8. In particular, datetime.fromisoformat() now tolerates surrogate unicode code points serving as the separator. Alexey Izbyshev provided the report and tests; Paul Ganssle wrote the patch.

[bpo-35066](https://bugs.python.org/issue?@action=redirect&bpo=35066): Formerly, invoking the strftime() method on a datetime object whose format string ended with a stray "%" raised an exception. That behavior, however, only appeared while the datetime C module was active; the python implementation behaved differently. Datetime is now PEP-399 compliant and will refrain from raising an exception over a trailing "%".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

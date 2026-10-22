# Python 3.9.0 alpha 1 / library / datetime

[bpo-37579](https://bugs.python.org/issue?@action=redirect&bpo=37579): To line up with the C implementation, the Python `__eq__` for [`timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) and [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) now hands back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) whenever the compared object is of a differing type. Karthikeyan Singaravelan wrote the patch.

[bpo-37685](https://bugs.python.org/issue?@action=redirect&bpo=37685): Repaired how [`datetime.timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) and [`datetime.timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone) values are compared.

[bpo-37642](https://bugs.python.org/issue?@action=redirect&bpo=37642): The pure Python build of [`datetime.timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone) may now express sub-minute offsets that sit near the minimum and maximum bounds, within the (23:59, 24:00) and (-23:59, 24:00) ranges specifically. Ngalim Siregar contributed the patch.

[bpo-38155](https://bugs.python.org/issue?@action=redirect&bpo=38155): Tahia Khan added `__all__` to [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

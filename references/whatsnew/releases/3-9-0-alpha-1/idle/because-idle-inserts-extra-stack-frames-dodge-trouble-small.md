# Python 3.9.0 alpha 1 / idle / because idle inserts extra stack frames dodge trouble small

[bpo-26806](https://bugs.python.org/issue?@action=redirect&bpo=26806): Because IDLE inserts extra stack frames and to dodge trouble with small recursion limits, the user code execution process raises its limits by 30. When those recursion limits are reported back, 30 is subtracted so the bump stays largely invisible.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

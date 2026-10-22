# Python 3.7.0 alpha 3 / core and builtins / traceback

[bpo-31949](https://bugs.python.org/issue?@action=redirect&bpo=31949): Several traceback-printing problems in PyTraceBack_Print() got fixed. A sys.tracebacklimit of 0 or below now stops tracebacks from being printed. Assigning None to sys.tracebacklimit now selects the default limit. Setting it to an integer above LONG_MAX now applies the limit LONG_MAX instead of the default. Integer overflows are corrected for the situation of more than `2**31` traceback items on Windows. Handling of output errors was also corrected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

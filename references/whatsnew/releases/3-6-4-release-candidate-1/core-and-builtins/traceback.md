# Python 3.6.4 release candidate 1 / core and builtins / traceback

[bpo-31949](https://bugs.python.org/issue?@action=redirect&bpo=31949): Repaired a number of problems while printing tracebacks (PyTraceBack_Print()). Assigning 0 or less to sys.tracebacklimit now stops tracebacks from printing. Assigning None to sys.tracebacklimit now means the default limit applies. Assigning an integer above LONG_MAX to sys.tracebacklimit now means the limit LONG_MAX is used instead of the default. Corrected integer overflows when there are more than `2**31` traceback items under Windows. Repaired handling of output errors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

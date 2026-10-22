# Python 3.6.3 release candidate 1 / tests / compiler and parser

[bpo-30822](https://bugs.python.org/issue?@action=redirect&bpo=30822): regrtest: Drop tzdata from regrtest --all. Whenever the suite runs through --use=all / -u all, tzdata is omitted because it slows test_datetime down so much (15-20 min on some buildbots) that it then exceeds the time limit on certain buildbots. This also repairs the regrtest command line parser to permit -u extralargefile so test_zipfile64 can run.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

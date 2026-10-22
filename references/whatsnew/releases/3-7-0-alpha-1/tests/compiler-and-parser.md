# Python 3.7.0 alpha 1 / tests / compiler and parser

[bpo-30822](https://bugs.python.org/issue?@action=redirect&bpo=30822): regrtest: Exclude tzdata from regrtest –all. While exercising the suite via –use=all / -u all, leave tzdata out, because it slows test_datetime down so much (15-20 min on certain buildbots) that those buildbots eventually time out. Also corrects the regrtest argument parser so that -u extralargefile can be passed to drive test_zipfile64.

[bpo-24932](https://bugs.python.org/issue?@action=redirect&bpo=24932): Adopt proper command line parsing within _testembed

[bpo-28409](https://bugs.python.org/issue?@action=redirect&bpo=28409): regrtest: repair the command line argument parser.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

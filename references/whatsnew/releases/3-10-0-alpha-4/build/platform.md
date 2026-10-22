# Python 3.10.0 alpha 4 / build / platform

[bpo-42604](https://bugs.python.org/issue?@action=redirect&bpo=42604): Every platform now derives its ?EXT_SUFFIX? build variable from SOABI (so on freeBSD, for example, ?EXT_SUFFIX? reads ?.cpython-310d.so? in place of ?.so?). Formerly only Linux, Mac and VxWorks used an ?EXT_SUFFIX? value carrying ?SOABI?.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

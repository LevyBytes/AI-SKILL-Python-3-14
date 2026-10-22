# Python 3.6.6 release candidate 1 / idle / text and unicode

[bpo-33204](https://bugs.python.org/issue?@action=redirect&bpo=33204): IDLE: color invalid string prefixes the same way every time. A ?u? string prefix may not be combined with either ?r? or ?f?. Starting from the right, color as much of the prefix as remains valid. The colorizer test was reworked and broadened.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

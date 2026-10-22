# Python 3.7.0 alpha 3 / windows / view fetch yields error no more items return none rather than raising msierror

[bpo-1102](https://bugs.python.org/issue?@action=redirect&bpo=1102): When `View.Fetch()` yields `ERROR_NO_MORE_ITEMS`, return `None` rather than raising `MSIError`. Anthony Tuininga provided the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

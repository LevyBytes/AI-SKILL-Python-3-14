# Python 3.6.4 release candidate 1 / windows / hand back none whenever view fetch yields error no more items rather than

[bpo-1102](https://bugs.python.org/issue?@action=redirect&bpo=1102): Hand back `None` whenever `View.Fetch()` yields `ERROR_NO_MORE_ITEMS`, rather than raising `MSIError`. Anthony Tuininga supplied the initial patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

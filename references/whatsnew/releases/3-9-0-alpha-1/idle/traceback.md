# Python 3.9.0 alpha 1 / idle / traceback

[bpo-35379](https://bugs.python.org/issue?@action=redirect&bpo=35379): On IDLE shutdown, swallow any AttributeError. Such an error arises when EditorWindow.close runs a second time. Emitting a traceback while IDLE runs from a terminal is both pointless and irritating.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

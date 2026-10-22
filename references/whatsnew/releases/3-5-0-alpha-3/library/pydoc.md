# Python 3.5.0 alpha 3 / library / pydoc

[bpo-23792](https://bugs.python.org/issue?@action=redirect&bpo=23792): Disregard KeyboardInterrupt while the pydoc pager runs. This echoes how the standard unix pagers act, and it keeps pipepager from terminating while the pager is itself still active.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

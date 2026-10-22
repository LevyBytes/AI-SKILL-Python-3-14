# What’s New in Python 2.7 / Two new environment variables for debug mode

### Two new environment variables for debug mode

Under debug mode, the `[xxx refs]` statistic isn't emitted by default; the `PYTHONSHOWREFCOUNT` environment variable now has to be set too. (Contributed by Victor Stinner; [bpo-31733](https://bugs.python.org/issue?@action=redirect&bpo=31733).)

When Python is built with `COUNT_ALLOC` defined, allocation counts are no longer dumped automatically anymore: the `PYTHONSHOWALLOCCOUNT` environment variable must now also be set. On top of that, allocation counts are now written to stderr instead of stdout. (Contributed by Victor Stinner; [bpo-31692](https://bugs.python.org/issue?@action=redirect&bpo=31692).)

Added in version 2.7.15.

[Subject index](INDEX.md) · [Previous source section](new-features-added-to-python-2-7-maintenance-releases.md) · [Next source section](pep-434-idle-enhancement-exception-for-all-branches.md) · [Release/subject declaration](the-future-for-python-2-x.md)

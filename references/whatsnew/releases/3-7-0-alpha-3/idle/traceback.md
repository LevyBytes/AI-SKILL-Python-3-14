# Python 3.7.0 alpha 3 / idle / traceback

[bpo-32207](https://bugs.python.org/issue?@action=redirect&bpo=32207): Better tk event exception tracebacks within IDLE. With tk event handling running under IDLE’s run loop, the puzzling and distracting queue.EMPTY traceback context is no longer attached to tk event exception tracebacks. That traceback now matches the one seen when user code drives event handling. The patch builds on a suggestion from Serhiy Storchaka.

[bpo-28603](https://bugs.python.org/issue?@action=redirect&bpo=28603): Repair a TypeError that triggered a shell restart while printing a traceback containing an unhashable exception. Zane Bitter wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

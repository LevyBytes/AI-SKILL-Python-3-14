# Python 3.6.4 release candidate 1 / idle / traceback

[bpo-32207](https://bugs.python.org/issue?@action=redirect&bpo=32207): Better tk event exception tracebacks within IDLE. Whenever tk event handling runs under IDLE’s run loop, a perplexing and distracting queue.EMPTY traceback context is no longer attached to tk event exception tracebacks. That traceback now matches what appears when user code drives event handling. The patch follows a suggestion from Serhiy Storchaka.

[bpo-28603](https://bugs.python.org/issue?@action=redirect&bpo=28603): Resolve a TypeError that triggered a shell restart while printing a traceback containing an exception that cannot be hashed. Zane Bitter contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

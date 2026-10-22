# Python 3.8.0 alpha 1 / library / queuehandler prepare duplicates record prior altering enqueueing other handlers further

[bpo-35726](https://bugs.python.org/issue?@action=redirect&bpo=35726): QueueHandler.prepare() now duplicates the record prior to altering and enqueueing it, so that other handlers further along the chain remain unaffected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

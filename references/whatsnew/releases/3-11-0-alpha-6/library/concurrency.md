# Python 3.11.0 alpha 6 / library / concurrency

[bpo-46752](https://bugs.python.org/issue?@action=redirect&bpo=46752): Bring task groups into asyncio (structured concurrency, modeled after Trio’s nurseries). Alongside that, task cancellation changes so that a cancelled task cannot be cancelled a second time until it invokes .uncancel().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

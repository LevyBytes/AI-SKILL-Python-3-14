# Python 3.5.0 alpha 4 / library / modules

[bpo-23865](https://bugs.python.org/issue?@action=redirect&bpo=23865): Across several modules, close() methods are now idempotent plus sturdier during shutdown. When multiple resources must be released, every one is freed even should errors arise.

[bpo-18473](https://bugs.python.org/issue?@action=redirect&bpo=18473): Repaired the 2to3 and 3to2 compatible pickle mappings. Resolved ambiguous reverse mappings. Many fresh mappings were added. The import mapping is no longer used on modules already covered by full name mapping.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

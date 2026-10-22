# Python 3.6.0 alpha 1 / library / collections

[bpo-26915](https://bugs.python.org/issue?@action=redirect&bpo=26915): Within the collections ABCs, the __contains__ methods now test identity ahead of testing equality. That aligns more closely with how the concrete classes behave, permits NaNs to be treated sensibly, and simplifies reasoning about container invariants.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

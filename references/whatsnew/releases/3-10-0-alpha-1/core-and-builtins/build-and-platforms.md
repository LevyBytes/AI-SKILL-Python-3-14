# Python 3.10.0 alpha 1 / core and builtins / build and platforms

[bpo-41670](https://bugs.python.org/issue?@action=redirect&bpo=41670): Stops line tracing from being dropped on platforms built without `USE_COMPUTED_GOTOS`. This addresses a case under Windows where certain lines inside a try-except block went untraced.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

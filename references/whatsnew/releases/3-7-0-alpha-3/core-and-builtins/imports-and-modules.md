# Python 3.7.0 alpha 3 / core and builtins / imports and modules

[bpo-21720](https://bugs.python.org/issue?@action=redirect&bpo=21720): No BytesWarning is emitted any longer when the *fromlist* argument passed to `__import__()`, or the module's `__all__` attribute, holds bytes instances.

[bpo-31786](https://bugs.python.org/issue?@action=redirect&bpo=31786): Corrects timeout rounding inside the select module so that negative timeouts in the range -1.0 to 0.0 round properly. These functions now block awaiting events the way they should; previously the call wrongly behaved as non-blocking. Pablo Galindo authored the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.6.4 release candidate 1 / core and builtins / imports and modules

[bpo-21720](https://bugs.python.org/issue?@action=redirect&bpo=21720): No BytesWarning is emitted any longer once the *fromlist* argument to `__import__()` or a module's `__all__` attribute holds bytes instances.

[bpo-31786](https://bugs.python.org/issue?@action=redirect&bpo=31786): Repair timeout rounding within the select module so negative timeouts in the range -1.0 to 0.0 round correctly. These functions now block while waiting for events as intended; formerly the call was wrongly non-blocking. Pablo Galindo supplied the patch.

[bpo-31642](https://bugs.python.org/issue?@action=redirect&bpo=31642): Brought back the ability to block “from package import module” by assigning None to sys.modules[“package.module”].

[bpo-31492](https://bugs.python.org/issue?@action=redirect&bpo=31492): Repair assertion failures that occurred when importing from a module bearing a bad `__name__` attribute fails, and when accessing an attribute of such a module fails. Oren Milman wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

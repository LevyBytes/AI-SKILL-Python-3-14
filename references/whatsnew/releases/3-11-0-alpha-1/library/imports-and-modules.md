# Python 3.11.0 alpha 1 / library / imports and modules

[bpo-44524](https://bugs.python.org/issue?@action=redirect&bpo=44524): The `typing` module classes gained the previously missing `__name__` and `__qualname__` attributes. Yurii Karabas supplied the patch.

[bpo-41249](https://bugs.python.org/issue?@action=redirect&bpo=41249): `TypedDict` was fixed so it cooperates with `typing.get_type_hints()` together with deferred annotation evaluation spanning modules.

[bpo-44554](https://bugs.python.org/issue?@action=redirect&bpo=44554): Argument handling inside `pdb.main()` was refactored to ease spotting errors while loading input and to make module-versus-script invocation behavior clearer.

[bpo-45124](https://bugs.python.org/issue?@action=redirect&bpo=45124): The `bdist_msi` command, which was deprecated in Python 3.9, has now been deleted.

Reach for `bdist_wheel` (wheel packages) as the replacement.

Hugo van Kemenade supplied this patch.

[bpo-35800](https://bugs.python.org/issue?@action=redirect&bpo=35800): `smtpd.MailmanProxy` has now been dropped because it cannot be used absent the external `mailman` module. Donghee Na wrote the patch.

[bpo-44747](https://bugs.python.org/issue?@action=redirect&bpo=44747): Reworked how `sys._getframe` gets used throughout the `typing` module. Yurii Karabas contributed the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

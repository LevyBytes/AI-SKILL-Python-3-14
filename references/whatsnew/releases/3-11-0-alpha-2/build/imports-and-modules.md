# Python 3.11.0 alpha 2 / build / imports and modules

[bpo-43158](https://bugs.python.org/issue?@action=redirect&bpo=43158): `setup.py` now draws on configure-script values to compile the `_uuid` extension module. Configure additionally picks up util-linux’s `libuuid` now.

[bpo-45548](https://bugs.python.org/issue?@action=redirect&bpo=45548): Improvements landed in `Modules/Setup` and `Modules/makesetup`. Functioning rules for every extension now live in the `Setup` file. Stale comments are gone. The rules `makesetup` emits handle dependencies accurately.

[bpo-45595](https://bugs.python.org/issue?@action=redirect&bpo=45595): Build dependencies on every Python header file plus module-specific header files are now tracked by `setup.py` and `makesetup`.

[bpo-43974](https://bugs.python.org/issue?@action=redirect&bpo=43974): `setup.py` stops defining `Py_BUILD_CORE_MODULE`. The macro is instead defined by each module that reaches into the internal API.

[bpo-45548](https://bugs.python.org/issue?@action=redirect&bpo=45548): Supply the absent entries within Modules/Setup.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

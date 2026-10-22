# Python 3.10.0 alpha 7 / library / imports and modules

[bpo-43428](https://bugs.python.org/issue?@action=redirect&bpo=43428): Pull in the updates from [importlib_metadata 3.7](https://importlib-metadata.readthedocs.io/en/latest/history.html#v3-7-0):

Distribution discovery got performance enhancements.

`entry_points` hands back only unique distributions now.

A new `EntryPoints` object arrives for holding a collection of entry points, with helper methods to pick entry points out by group or by name. When selection parameters are passed, `entry_points` returns this object, though it still yields a dict object for backward compatibility. The recommendation is to lean on the selection interface. Expect the dict object result to be deprecated down the line.

A packages_distributions function was added; it yields a mapping from packages to the distributions supplying them.

[bpo-41282](https://bugs.python.org/issue?@action=redirect&bpo=41282): Corrected the stacklevel of the `DeprecationWarning` raised by `import distutils`.

[bpo-40066](https://bugs.python.org/issue?@action=redirect&bpo=40066): The `repr()` and `str()` of Enum members were revised: `repr()` is now *EnumClass.MemberName*, while `str()` is *MemberName*. On top of that, stdlib Enums whose members surface as module attributes (`RegexFlag.IGNORECASE`, for instance) carry a `repr()` of *module.name* — that is, `re.IGNORECASE`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

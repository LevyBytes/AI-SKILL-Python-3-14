# Python 3.7.0 alpha 1 / library / imports and modules

[bpo-27611](https://bugs.python.org/issue?@action=redirect&bpo=27611): Restored default-root-window support within the tkinter.tix module. A master parameter was added to the DisplayStyle constructor.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Assorted typing module changes: typing.NoReturn was added, WrapperDescriptorType is now used, and minor bugs were fixed. Jim Fasarakis-Hilliard and Ivan Levkivskyi authored the original PRs.

[bpo-25464](https://bugs.python.org/issue?@action=redirect&bpo=25464): Repaired HList.header_exists() inside the tkinter.tix module by adding a workaround for a Tix library bug.

[bpo-23214](https://bugs.python.org/issue?@action=redirect&bpo=23214): Inside the “io” module, BufferedReader and BytesIO’s read1() methods now take an optional argument that may be -1, in keeping with the BufferedIOBase specification.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): The `typing` module gained speed improvements. Ivan Levkivskyi and Mitar authored the original PRs.

[bpo-31544](https://bugs.python.org/issue?@action=redirect&bpo=31544): ElementTree's C accelerator module disregarded exceptions that were raised during the lookup of TreeBuilder target methods inside XMLParser().

[bpo-28182](https://bugs.python.org/issue?@action=redirect&bpo=28182): The SSL module now raises SSLCertVerificationError whenever OpenSSL fails to verify the peer's certificate. That exception carries richer information about the error.

[bpo-28325](https://bugs.python.org/issue?@action=redirect&bpo=28325): Deleted the obsolete MacOS 9 macurl2path module together with its tests.

[bpo-29851](https://bugs.python.org/issue?@action=redirect&bpo=29851): Should a module have no spec, importlib.reload() now raises ModuleNotFoundError.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): More typing module changes: typing.Counter, typing.ChainMap, better ABC caching, and so on. The original PRs came from Jelle Zijlstra, Ivan Levkivskyi, Manuel Krebber, and Łukasz Langa.

[bpo-29377](https://bugs.python.org/issue?@action=redirect&bpo=29377): The built-in types WrapperDescriptorType, MethodWrapperType, and MethodDescriptorType were added to the types module. Manuel Krebber supplied the original patch.

[bpo-30946](https://bugs.python.org/issue?@action=redirect&bpo=30946): Drop obsolete code from the readline module covering platforms where GNU readline predates 2.1 or where select() is unavailable.

[bpo-29741](https://bugs.python.org/issue?@action=redirect&bpo=29741): Bring several methods of the _pyio module up to accepting integer types as well. Oren Milman wrote the patch.

[bpo-30436](https://bugs.python.org/issue?@action=redirect&bpo=30436): When the named parent module is not a package (that is, it lacks a __path__ attribute), importlib.find_spec() now raises ModuleNotFoundError rather than AttributeError.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): typing module changes: a generic AsyncContextManager was added, and ContextManager gained support across all versions. Jelle Zijlstra and Ivan Levkivskyi authored the original PRs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

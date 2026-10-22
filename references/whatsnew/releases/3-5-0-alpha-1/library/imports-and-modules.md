# Python 3.5.0 alpha 1 / library / imports and modules

[bpo-20383](https://bugs.python.org/issue?@action=redirect&bpo=20383): importlib.util.module_from_spec() was introduced as the recommended means of creating a new module.

[bpo-21226](https://bugs.python.org/issue?@action=redirect&bpo=21226): Modules are now configured properly within PyImport_ExecCodeModuleObject (and friends).

[bpo-21905](https://bugs.python.org/issue?@action=redirect&bpo=21905): A RuntimeError in pickle.whichmodule() is avoided for when sys.modules gets mutated mid-iteration. Olivier Grisel supplied the patch.

[bpo-1218234](https://bugs.python.org/issue?@action=redirect&bpo=1218234): inspect.getsource() was fixed so it reads the refreshed source from a reloaded module. Berker Peksag wrote the first patch.

[bpo-21971](https://bugs.python.org/issue?@action=redirect&bpo=21971): The turtledemo doc was updated and the module was indexed.

[bpo-21407](https://bugs.python.org/issue?@action=redirect&bpo=21407): _decimal: function signatures are now supported by the module.

[bpo-21729](https://bugs.python.org/issue?@action=redirect&bpo=21729): The dbm.dumb module now wraps file handling in a ?with? statement so files are reliably closed. Claudiu Popa wrote the patch.

[bpo-21966](https://bugs.python.org/issue?@action=redirect&bpo=21966): When the code module is executed, the -q command-line option is now honored.

[bpo-21863](https://bugs.python.org/issue?@action=redirect&bpo=21863): Alongside their own name, cProfile now shows the module name of C extension functions.

[bpo-15275](https://bugs.python.org/issue?@action=redirect&bpo=15275): The ntpath module was cleaned up and made faster.

[bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662): Whenever a package's `__init__.py` defines `load_tests()`, that hook now runs every time without exception. The use_load_tests keyword is still tolerated by `TestLoader.loadTestsFromModule()`, yet it carries a deprecation and has no effect. The method also gains a documented keyword-only `pattern` attribute. Robert Collins authored the patch and Barry Warsaw refined it.

[bpo-20633](https://bugs.python.org/issue?@action=redirect&bpo=20633): A relative import was swapped out for an absolute import.

[bpo-19165](https://bugs.python.org/issue?@action=redirect&bpo=19165): Rather than PendingDeprecationWarning, the formatter module now raises DeprecationWarning.

[bpo-23093](https://bugs.python.org/issue?@action=redirect&bpo=23093): Within the io, module, additional operations are now permitted on detached streams.

[bpo-13968](https://bugs.python.org/issue?@action=redirect&bpo=13968): The glob module now allows recursive searching through subdirectories via the `**` pattern.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

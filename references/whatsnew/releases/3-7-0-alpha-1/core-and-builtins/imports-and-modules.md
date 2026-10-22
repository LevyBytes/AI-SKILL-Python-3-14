# Python 3.7.0 alpha 1 / core and builtins / imports and modules

[bpo-30876](https://bugs.python.org/issue?@action=redirect&bpo=30876): A relative import from a package that isn't loaded now reimports that package rather than blowing up with SystemError. A relative import from something that isn't a package now blows up with ImportError instead of SystemError.

[bpo-30024](https://bugs.python.org/issue?@action=redirect&bpo=30024): Circular imports that involve absolute imports and bind a submodule to a name are now handled.

[bpo-29546](https://bugs.python.org/issue?@action=redirect&bpo=29546): On ImportError for `from ... import ...`, set the 'path' and 'name' attribute.

[bpo-29546](https://bugs.python.org/issue?@action=redirect&bpo=29546): Sharpen the from-import error message with a location

[bpo-28411](https://bugs.python.org/issue?@action=redirect&bpo=28411): Replace direct references to PyInterpreterState.modules with PyImport_GetModuleDict(). On top of that, bring more consistency to other code touching sys.modules. Doing so cuts down on the headaches involved in working on sys.modules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

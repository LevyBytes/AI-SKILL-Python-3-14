# Python 3.14.0 alpha 1 / library / imports and modules

[gh-118908](https://github.com/python/cpython/issues/118908): Restrict the globals exposed by internal imports and definitions whenever a new REPL starts up. Eugene Triguba and Pablo Galindo authored the patch.

[gh-121245](https://github.com/python/cpython/issues/121245): Streamline how the `site.register_readline()` helper deals with the history file. The `CAN_USE_PYREPL` variable will now be set up at import time. Patch by Sergey B Kirpichev.

[gh-119594](https://github.com/python/cpython/issues/119594): When pow(fractions.Fraction, x, module) is called with modulo set to something other than None, the message now explains that the types do not mix, rather than claiming pow accepts only 2 arguments. Wim Jeantine-Glenn and Mark Dickinson wrote the patch.

[gh-118673](https://github.com/python/cpython/issues/118673): Shebang lines and executable bits are now cleared from stdlib modules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

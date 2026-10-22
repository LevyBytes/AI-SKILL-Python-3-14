# Python 3.13.0 alpha 1 / tools demos / compiler and parser

[gh-107704](https://github.com/python/cpython/issues/107704): Argument Clinic can now flag keyword arguments as deprecated for keyword-or-positional parameters, by way of the fresh `/ [from X.Y]` syntax. (Read it as *?positional-only from Python version X.Y?*.) Further details live in the [documentation in the Python Developer's Guide](https://devguide.python.org/development-tools/clinic/#clinic-howto-deprecate-keyword).

[gh-106970](https://github.com/python/cpython/issues/106970): Several bugs in the Argument Clinic `destination <name> clear` command are corrected: the destination buffers were left uncleared, and after running the command the `destination` directive parser merely fell through to the fault handler. Erlend E. Aasland provided this fix.

[gh-106706](https://github.com/python/cpython/issues/106706): Adjust the bytecode syntax used for families so that the redundant name-matching pseudo syntax is gone.

[gh-95065](https://github.com/python/cpython/issues/95065): Passing parameters positionally can now be marked deprecated in Argument Clinic via the new `* [from X.Y]` syntax. (Read it as *?keyword-only from Python version X.Y?*.) More background is in the [documentation in the Python Developer's Guide](https://devguide.python.org/development-tools/clinic/#clinic-howto-deprecate-positional). Erlend E. Aasland authored this, with assistance from Alex Waygood, Nikita Sobolev, and Serhiy Storchaka.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

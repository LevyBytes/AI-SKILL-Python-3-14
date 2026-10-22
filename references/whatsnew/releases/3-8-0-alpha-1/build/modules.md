# Python 3.8.0 alpha 1 / build / modules

[bpo-35011](https://bugs.python.org/issue?@action=redirect&bpo=35011): Brings back pyexpatns.h so that our bundled copy of the expat C library is isolated, keeping its symbols from clashing during link or dynamic-load time with an embedding program or with other extension modules carrying their own libexpat.

[bpo-33394](https://bugs.python.org/issue?@action=redirect&bpo=33394): Turn on the verbose build for extension modules whenever GNU make receives macros on its command line.

[bpo-32232](https://bugs.python.org/issue?@action=redirect&bpo=32232): By default the modules set up in `Modules/Setup` are henceforth compiled without `-DPy_BUILD_CORE`. Modules that genuinely require that preprocessor definition list it within their own entries instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

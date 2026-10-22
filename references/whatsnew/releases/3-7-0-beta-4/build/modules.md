# Python 3.7.0 beta 4 / build / modules

[bpo-33394](https://bugs.python.org/issue?@action=redirect&bpo=33394): Turn on verbose builds for extension modules whenever GNU make receives macros on the command line.

[bpo-32232](https://bugs.python.org/issue?@action=redirect&bpo=32232): By default, the modules configured under `Modules/Setup` are no longer compiled with `-DPy_BUILD_CORE`. Instead, any module that truly requires that preprocessor definition lists it in its own individual entry.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

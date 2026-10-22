# Python 3.8.0 alpha 1 / build / compiler and parser

[bpo-35550](https://bugs.python.org/issue?@action=redirect&bpo=35550): Correct the faulty Solaris #ifdef tests so they check for __sun && __SVR4 rather than sun during compilation.

[bpo-34585](https://bugs.python.org/issue?@action=redirect&bpo=34585): Detect floating-point byte order within configure.ac via compilation tests rather than by running code, so the checks also succeed for cross-compiled builds.

[bpo-33483](https://bugs.python.org/issue?@action=redirect&bpo=33483): The C compiler is henceforth identified accurately from the usual environment variables. The –without-gcc and –with-icc options were dropped.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

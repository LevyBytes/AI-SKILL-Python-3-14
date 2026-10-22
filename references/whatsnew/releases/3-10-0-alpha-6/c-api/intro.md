# Python 3.10.0 alpha 6 / c api / intro

[bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134): The headers odictobject.h, parser_interface.h, picklebufobject.h, pydebug.h, and pyfpe.h were relocated under the cpython/ directory. Including them on their own is forbidden, since Python.h already pulls them in: [Include Files](https://docs.python.org/3.14/c-api/intro.html#api-includes).

[bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134): The headers pyarena.h, pyctype.h, and pytime.h were relocated under the cpython/ directory. Including them on their own is forbidden, since Python.h already pulls them in: [Include Files](https://docs.python.org/3.14/c-api/intro.html#api-includes).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

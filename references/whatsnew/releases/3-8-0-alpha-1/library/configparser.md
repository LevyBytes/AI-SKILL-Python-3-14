# Python 3.8.0 alpha 1 / library / configparser

[bpo-33504](https://bugs.python.org/issue?@action=redirect&bpo=33504): Move the default dictionary backing [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) away from [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) over to the ordinary [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) type.

[bpo-32108](https://bugs.python.org/issue?@action=redirect&bpo=32108): Within configparser, a section is no longer cleared when it gets assigned to itself.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

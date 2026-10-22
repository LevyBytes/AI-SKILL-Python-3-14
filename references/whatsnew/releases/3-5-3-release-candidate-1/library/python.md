# Python 3.5.3 release candidate 1 / library / python

[bpo-29119](https://bugs.python.org/issue?@action=redirect&bpo=29119): Repair weakrefs within the pure-python collections.OrderedDict move_to_end() method. Andra Bogildea contributed this.

A fresh build of typing.py pulled from [https://github.com/python/typing](https://github.com/python/typing) brings several upstream items. It introduces Collection (only for 3.6) ([bpo-27598](https://bugs.python.org/issue?@action=redirect&bpo=27598)). It puts FrozenSet into __all__ (upstream #261). It clears a crash within _get_type_vars() (upstream #259). And it lifts the dict constraint out of ForwardRef._eval_type (upstream #252).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

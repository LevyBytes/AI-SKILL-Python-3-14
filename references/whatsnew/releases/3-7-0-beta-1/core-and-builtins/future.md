# Python 3.7.0 beta 1 / core and builtins / future

[bpo-32670](https://bugs.python.org/issue?@action=redirect&bpo=32670): Enforce [**PEP 479**](https://peps.python.org/pep-0479/) across all code. What this means is that manually raising a StopIteration exception out of a generator is forbidden for all code, no matter whether "from __future__ import generator_stop" was applied or not.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

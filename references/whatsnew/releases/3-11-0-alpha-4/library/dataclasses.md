# Python 3.11.0 alpha 4 / library / dataclasses

[bpo-44674](https://bugs.python.org/issue?@action=redirect&bpo=44674): Alter the way dataclasses reject mutable default values. The old approach relied on a list of known types (list, dict, set); the new one forbids unhashable objects as defaults, treating unhashability as a stand-in for mutability. Eric V. Smith wrote the patch, with the idea coming from Raymond Hettinger.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

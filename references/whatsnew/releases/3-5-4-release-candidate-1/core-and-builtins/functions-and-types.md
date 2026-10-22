# Python 3.5.4 release candidate 1 / core and builtins / functions and types

[bpo-25794](https://bugs.python.org/issue?@action=redirect&bpo=25794): Corrected type.__setattr__() along with type.__delattr__() for attribute names that are not interned. Founded on a patch from Eryk Sun.

[bpo-29602](https://bugs.python.org/issue?@action=redirect&bpo=29602): Repair the mishandling of signed zeros in the complex constructor for complex subclasses and for inputs that carry a __complex__ method. Serhiy Storchaka supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.7.0 alpha 1 / library / configparser

[bpo-24142](https://bugs.python.org/issue?@action=redirect&bpo=24142): Parsing a corrupt config file used to leave configparser sitting in an invalid state. Florian Höch supplied the original patch.

[bpo-23835](https://bugs.python.org/issue?@action=redirect&bpo=23835): configparser: defaults are now read inside the `ConfigParser()` constructor through `read_dict()`, which lines the behavior up with how the remainder of the parser behaves. Keys and values in the defaults dictionary that are not strings now get converted to strings implicitly. James Tocknell wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.9.0 beta 1 / library / argparse

[bpo-39058](https://bugs.python.org/issue?@action=redirect&bpo=39058): Within the argparse module, the repr produced for Namespace() plus other argument holders at this point follows the sequence in which attributes joined. Previously it followed alphabetical order, although argument ordering stays intact across the user visible parts of the module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

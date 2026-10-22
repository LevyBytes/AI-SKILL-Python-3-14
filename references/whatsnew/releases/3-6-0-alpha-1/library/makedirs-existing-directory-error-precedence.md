# Python 3.6.0 alpha 1 / library / sidestep spurious errors os makedirs exist ok true reported whenever os

[bpo-25583](https://bugs.python.org/issue?@action=redirect&bpo=25583): Sidestep the spurious errors that os.makedirs(exist_ok=True) reported whenever the OS ranks errors like EACCES ahead of EEXIST.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

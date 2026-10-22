# Python 3.11.0 alpha 1 / library / argparse

[bpo-38956](https://bugs.python.org/issue?@action=redirect&bpo=38956): The default value of [`argparse.BooleanOptionalAction`](https://docs.python.org/3.14/library/argparse.html#argparse.BooleanOptionalAction) stops appearing twice once it is combined with [`argparse.ArgumentDefaultsHelpFormatter`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter).

[bpo-45235](https://bugs.python.org/issue?@action=redirect&bpo=45235): Resolved a defect where argparse dropped values held in a supplied namespace once a subparser carrying defaults was involved.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

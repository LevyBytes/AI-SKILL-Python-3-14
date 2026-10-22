# Python 3.11.0 alpha 5 / core and builtins / platform

[bpo-46406](https://bugs.python.org/issue?@action=redirect&bpo=46406): The floor-division operator `//` has been reworked so the compiler grasps its constraints more readily. On the amd64 platform it can run 20% quicker when an int is divided by something below `2**30`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

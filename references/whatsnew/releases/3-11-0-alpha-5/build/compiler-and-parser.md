# Python 3.11.0 alpha 5 / build / compiler and parser

[bpo-46600](https://bugs.python.org/issue?@action=redirect&bpo=46600): Repair the check in the `./configure` script that decides whether the C compiler accepts the `-Og` option, so it likewise applies `-Og` on clang where it is supported. Victor Stinner authored the patch.

[bpo-38472](https://bugs.python.org/issue?@action=redirect&bpo=38472): Repair GCC detection within setup.py during cross-compilation. The C compiler now executes under LC_ALL=C. Earlier the detection broke with a German locale.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

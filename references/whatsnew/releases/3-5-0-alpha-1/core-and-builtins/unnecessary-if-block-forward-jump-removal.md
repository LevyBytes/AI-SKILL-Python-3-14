# Python 3.5.0 alpha 1 / core and builtins / steer clear emitting jump forward instruction close if block whenever no

[bpo-11471](https://bugs.python.org/issue?@action=redirect&bpo=11471): steer clear of emitting a JUMP_FORWARD instruction at the close of an if-block whenever no else-clause exists. Eugene Toder wrote the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

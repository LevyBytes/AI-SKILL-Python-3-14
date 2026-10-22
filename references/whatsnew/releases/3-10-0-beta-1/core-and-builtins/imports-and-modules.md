# Python 3.10.0 beta 1 / core and builtins / imports and modules

[bpo-43901](https://bugs.python.org/issue?@action=redirect&bpo=43901): Module and class objects were switched to building their empty annotations dicts lazily, only once requested. Those annotations dicts continue living in the object's __dict__ so older code keeps working.

[bpo-43963](https://bugs.python.org/issue?@action=redirect&bpo=43963): Importing the `_signal` module within a subinterpreter no longer carries side effects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

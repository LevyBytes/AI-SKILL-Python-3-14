# Python 3.9.0 alpha 4 / core and builtins / tuned pattern assigning temporary variable inside comprehensions

[bpo-32856](https://bugs.python.org/issue?@action=redirect&bpo=32856): Tuned the pattern for assigning a temporary variable inside comprehensions. The `for y in [expr]` construct in comprehensions now matches the speed of a plain assignment `y = expr`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

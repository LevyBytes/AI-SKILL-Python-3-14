# Python 3.7.0 alpha 3 / core and builtins / collections and iteration

[bpo-10544](https://bugs.python.org/issue?@action=redirect&bpo=10544): Comprehensions and generator expressions now treat yield expressions as deprecated. Such expressions remain allowed inside the definition of the outermost iterable, since that part is evaluated directly within the surrounding scope.

[bpo-32023](https://bugs.python.org/issue?@action=redirect&bpo=32023): A SyntaxError is now properly emitted whenever a parenthesis-free generator expression stands in for an inheritance list within a class definition. Dropping the duplicated parentheses is permitted only on calls.

[bpo-32012](https://bugs.python.org/issue?@action=redirect&bpo=32012): A SyntaxError is now properly emitted whenever a parenthesis-free generator expression is handed in as an argument yet trailed by a comma. Such an expression must sit directly inside a set of parentheses and may not carry a comma on either flank.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

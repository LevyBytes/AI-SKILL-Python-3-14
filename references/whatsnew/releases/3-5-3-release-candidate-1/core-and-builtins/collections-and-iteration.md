# Python 3.5.3 release candidate 1 / core and builtins / collections and iteration

[bpo-27812](https://bugs.python.org/issue?@action=redirect&bpo=27812): Clear a generator's frame's backreference to that generator properly, avoiding crashes inside frame.clear().

[bpo-26020](https://bugs.python.org/issue?@action=redirect&bpo=26020): The evaluation order for a set literal did not align with the documented behaviour.

[bpo-28512](https://bugs.python.org/issue?@action=redirect&bpo=28512): Correct how the offset attribute of SyntaxError gets set by PyErr_SyntaxLocationEx() and PyErr_SyntaxLocationObject().

[bpo-28376](https://bugs.python.org/issue?@action=redirect&bpo=28376): The long range iterator type is now registered as an Iterator. Oren Milman contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

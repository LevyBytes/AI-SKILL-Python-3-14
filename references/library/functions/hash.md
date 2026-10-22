# hash

hash(*object*, */*)

Return the hash value of the object (when it has one). Hash values are integers. They serve to compare dictionary keys quickly while a dictionary lookup happens. Numeric values that compare equal share an identical hash value (even when their types differ, which is the situation with 1 and 1.0).

Note

For objects carrying custom [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) methods, be aware that `hash()` truncates the returned value according to the host machine's bit width.

[Builtin task index](INDEX.md).

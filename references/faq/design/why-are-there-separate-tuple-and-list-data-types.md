# Why are there separate tuple and list data types?

### Why are there separate tuple and list data types?

Although lists and tuples resemble one another in many ways, they are usually put to fundamentally different uses. You can picture tuples as akin to Pascal `records` or C `structs`; they are small collections of related data, possibly of differing types, that get handled as a unit. A Cartesian coordinate, for instance, is well represented by a tuple of two or three numbers.

Lists, by contrast, behave more like arrays found in other languages. They typically hold a varying count of objects that all share the same type and that get processed one at a time. For instance, [`os.listdir('.')`](https://docs.python.org/3.14/library/os.html#os.listdir) hands back a list of strings naming the files in the current directory. Functions operating on that output would generally keep working even if you dropped another file or two into the directory.

Tuples are immutable, which means that once you've created a tuple, none of its elements can be swapped out for a new value. Lists are mutable, which means a list's elements can always be changed. Only immutable elements may serve as dictionary keys, and so tuples but not lists are usable as keys.

[Subject index](INDEX.md)

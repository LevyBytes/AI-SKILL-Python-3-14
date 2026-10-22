# How do I get a list of all instances of a given class?

### How do I get a list of all instances of a given class?

Python keeps no registry of every instance of a class (nor of a built-in type). You can have the class’s constructor record each instance by maintaining a list of weak references to them.

[Subject index](INDEX.md)

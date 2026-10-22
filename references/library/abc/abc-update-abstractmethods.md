# abc: `abc.update_abstractmethods()`

abc.update_abstractmethods(*cls*)

A function that recomputes an abstract class's abstraction status. Call it whenever a class's abstract methods get implemented or altered after the class was created. As a rule, you would call it from inside a class decorator.

Hands back *cls*, so it can serve as a class decorator.

Where *cls* is not an instance of `ABCMeta`, it has no effect.

Note

This function takes for granted that the superclasses of *cls* have already been refreshed, and it refreshes no subclasses of its own.

Added in version 3.10.

Footnotes

[Subject index](INDEX.md) · [Previous](abc-get-cache-token.md) · [Continue](../aifc/aifc-read-and-write-aiff-and-aifc-files.md) · [Owning module, declaration or section: abc](abc-abc-class.md)

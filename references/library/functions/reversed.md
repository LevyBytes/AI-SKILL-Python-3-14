# reversed

reversed(*object*, */*)

Hand back a reverse [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). Whatever you pass has to be an object that either provides a [`__reversed__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__reversed__) method or honors the sequence protocol (that is, the [`__len__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__len__) method together with the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method taking integer arguments that begin at `0`).

[Builtin task index](INDEX.md).

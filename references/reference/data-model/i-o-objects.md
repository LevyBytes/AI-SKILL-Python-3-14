# 3.2.12. I/O objects (also known as file objects)

### 3.2.12. I/O objects (also known as file objects)

An open file is represented by a [file object](https://docs.python.org/3.14/glossary.html#term-file-object). Several conveniences exist for producing file objects: the [`open()`](https://docs.python.org/3.14/library/functions.html#open) built-in function, plus [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen), [`os.fdopen()`](https://docs.python.org/3.14/library/os.html#os.fdopen), and the [`makefile()`](https://docs.python.org/3.14/library/socket.html#socket.socket.makefile) method belonging to socket objects (and possibly through additional functions or methods supplied by extension modules).

To make them easier to work with in generic code, file objects expose the shared methods catalogued below. They are anticipated to behave as With Statement Context Managers.

`sys.stdin`, `sys.stdout` and `sys.stderr` are set up at startup as file objects tied to the interpreter’s standard input, output and error streams; each one opens in text mode and consequently conforms to the interface laid out by the [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) abstract class.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Following source section](object-dict.md) · [Previous source section](object-dict.md) · [Following source section](file-read.md)

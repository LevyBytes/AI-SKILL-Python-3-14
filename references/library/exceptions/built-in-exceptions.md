# Built-in Exceptions

### Built-in Exceptions

Every exception in Python has to be an instance of some class descending from `BaseException`. Within a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement whose [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause names a given class, that same clause will also catch any exception classes that descend from it (though not the classes *it* itself descends from). When two exception classes share no subclass relationship, they are never treated as equal, even should they carry an identical name.

The interpreter or its built-in functions may produce the built-in exceptions catalogued in this chapter. Unless otherwise noted, each carries an "associated value" that spells out the precise cause of the failure. That value might be a string, or it might be a tuple bundling several pieces of information together (for instance, an error code paired with a string that explains the code). Typically the associated value is handed to the constructor of the exception class as arguments.

It is permissible for user code to raise the built-in exceptions itself. Doing so lets you exercise an exception handler, or flag an error condition "just like" the case where the interpreter would have raised that same exception; keep in mind, though, that nothing stops user code from raising an exception that does not fit the situation.

You may subclass the built-in exception classes to build your own exceptions; the recommendation is that programmers descend their new exceptions from the `Exception` class or one of its descendants, rather than from `BaseException`. The Python Tutorial covers how to define exceptions in greater depth under [User-defined Exceptions](https://docs.python.org/3.14/tutorial/errors.html#tut-userexceptions).

[Subject index](INDEX.md) · [Continue](baseexception-context-to-baseexception-suppress-context.md)

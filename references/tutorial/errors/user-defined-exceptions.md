# 8.6. User-defined Exceptions

### 8.6. User-defined Exceptions

A program is free to introduce exceptions of its own by defining a fresh exception class (consult [Classes](https://docs.python.org/3.14/tutorial/classes.html#tut-classes) for further detail on Python classes). As a rule, such exceptions ought to descend from the [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) class, whether straight away or by way of an intermediary.

You can give exception classes any behavior another class might have, but they're commonly kept lean, frequently exposing nothing more than a handful of attributes through which handlers can pull details about the error.

The majority of exceptions carry names finishing in "Error", echoing how the standard exceptions are named.

A good many standard modules set up exceptions of their own to flag errors that might arise within the functions they provide.

[Subject index](INDEX.md) · [Previous source section](exception-chaining.md) · [Following source section](defining-clean-up-actions.md)

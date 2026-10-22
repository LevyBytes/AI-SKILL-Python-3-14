# 8.2. Exceptions

### 8.2. Exceptions

A statement or expression can be flawless syntactically and still trigger an error once you try to run it. The errors that show up while running are termed *exceptions*, and they don't always have to be fatal: shortly you'll learn how to deal with them in your Python programs. Still, the bulk of exceptions go unhandled by programs and end up as error messages like the ones below:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str

```

What occurred is reported by the final line of the error message. Exceptions arrive in assorted types, and that type appears as part of the text: the ones in this example are [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError), [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) and [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). What's shown as the exception type corresponds to the name of whichever built-in exception was raised. That holds for every built-in exception, though it isn't guaranteed for ones you define yourself (even if following the convention is handy). The names of standard exceptions are built-in identifiers (they are not reserved keywords).

Whatever follows on that line supplies specifics that depend on the exception type and its trigger.

The earlier portion of the error message presents the setting in which the exception arose, rendered as a stack traceback. Typically it carries a stack traceback that lists source lines; it won't, however, show lines that were read from standard input.

[Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html#bltin-exceptions) lists the built-in exceptions and their meanings.

[Subject index](INDEX.md) · [Previous source section](syntax-errors.md) · [Following source section](exception-handler-dispatch-and-inheritance.md)

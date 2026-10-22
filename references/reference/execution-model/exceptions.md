# 4.3. Exceptions

### 4.3. Exceptions

Exceptions provide a way to break out of a code block's normal flow of control so as to deal with errors or other out-of-the-ordinary conditions. An exception is *raised* at the spot where the error gets detected; the surrounding code block, or any code block that called the offending code block whether directly or indirectly, may *handle* it.

Upon detecting a run-time error (division by zero, say), the Python interpreter raises an exception. A Python program is also free to raise an exception of its own accord using the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement. You set up exception handlers with the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) statement. The [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause of one of those statements lets you name cleanup code that does not handle the exception but runs regardless of whether an exception arose in the code that came before.

For error handling Python adopts the "termination" model: an exception handler can learn what went wrong and carry on at an outer level, but it has no way to mend the underlying cause and re-attempt the operation that failed (short of re-entering the offending stretch of code from its start).

Where an exception goes entirely unhandled, the interpreter ends the program's execution, or else drops back to its interactive main loop. Either way it prints a stack traceback — the lone exception being when the exception is [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit).

Class instances are what identify exceptions. Which [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause gets picked turns on the instance's class: the clause must name the instance's class or a [non-virtual base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) of it. The handler is able to receive the instance, which can convey further detail about the exceptional condition.

Note

The Python API does not include exception messages. What they contain is liable to shift from one Python version to the next with no warning, so code meant to run under several interpreter versions should not lean on them.

Consult as well the account of the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement in section [The try statement](https://docs.python.org/3.14/reference/compound_stmts.html#try) and of the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement in section [The raise statement](https://docs.python.org/3.14/reference/simple_stmts.html#raise).

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Previous source section](interaction-with-dynamic-features.md) · [Following source section](general-computing-model.md)

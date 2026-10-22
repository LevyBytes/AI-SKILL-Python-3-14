# Extending and Embedding the Python Interpreter

# Extending

### Extending and Embedding the Python Interpreter

Here you'll learn to author C or C++ modules that add fresh modules to the Python interpreter. Such modules are free to introduce new functions, and they can equally well supply brand-new object types together with the methods on those types. Beyond that, this text walks through embedding the Python interpreter within some other program so it can serve as that program's extension language. The closing material explains how you compile and link your extension modules to make them loadable on the fly (during run time) by the interpreter, provided the host operating system permits dynamic loading.

A working familiarity with Python is taken for granted throughout this text. Should you want a relaxed first tour of the language, turn to [The Python Tutorial](https://docs.python.org/3.14/tutorial/index.html#tutorial-index). A stricter, more rigorous specification lives in [The Python Language Reference](https://docs.python.org/3.14/reference/index.html#reference-index). Meanwhile, [The Python Standard Library](https://docs.python.org/3.14/library/index.html#library-index) catalogs the object types, functions, and modules already available — whether built in or coded in Python — that lend the language its broad reach.

When you need the complete rundown of the entire Python/C API, consult its dedicated [Python/C API reference manual](https://docs.python.org/3.14/c-api/index.html#c-api-index).

[Subject index](INDEX.md) · [Next source section](recommended-third-party-tools.md)

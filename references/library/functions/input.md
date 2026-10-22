# Built-in Functions

input()

 input(*prompt*, */*)

When the *prompt* argument is supplied, it gets written to standard output with no trailing newline. The function next reads one line from input, turns it into a string (dropping a trailing newline), and returns it. Reading EOF triggers an [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError). Example:

```python
>>> s = input('--> ')
--> Monty Python's Flying Circus
>>> s
"Monty Python's Flying Circus"

```

When the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module has been loaded, `input()` will draw on it to deliver rich line editing and history capabilities.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `builtins.input` with argument `prompt` before reading input

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `builtins.input/result` with the result after successfully reading input.

[Subject index](INDEX.md) · [Previous](INDEX.md) · [Continue](int-class-to-int-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)

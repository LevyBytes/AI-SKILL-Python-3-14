# 2.1.2. Interactive Mode

### 2.1.2. Interactive Mode

Whenever commands arrive from a tty, the interpreter is described as being in *interactive mode*. While there, it asks for the next command using the *primary prompt*, normally three greater-than signs (`>>>`); on continuation lines it switches to the *secondary prompt*, three dots by default (`...`). Ahead of that first prompt, the interpreter prints a welcome message giving its version number along with a copyright notice:

```shell
$ python3.14
Python 3.14 (default, April 4 2024, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

Whenever you key in a multi-line construct, continuation lines come into play. For an illustration, consider this [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement:

```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!

```

Further detail on interactive mode lives at [Interactive Mode](https://docs.python.org/3.14/tutorial/appendix.html#tut-interac).

[Subject index](INDEX.md) · [Previous source section](argument-passing.md) · [Following source section](source-code-encoding.md)

# codeop: `codeop.compile_command()`

# Codeop, Collections.Abc

## Overview

Covers: codeop — Compile Python code??; collections.abc — Abstract Base Classes for Containers??.

## codeop - Compile Python code??

### `codeop` - Compile Python code

**Source code:** [Lib/codeop.py](https://github.com/python/cpython/tree/3.14/Lib/codeop.py)

---

The building blocks that let you emulate Python's read-eval-print loop live in the `codeop` module, just as the [`code`](https://docs.python.org/3.14/library/code.html#module-code) module already does. For that reason, reaching for this module directly is rarely what you want; should you need such a loop inside your own program, the `code` module is the better choice.

This task breaks down into two parts:

1.

Detecting when a line of input finishes a Python statement — that is, deciding whether the next prompt should be "`>>>`" or "`...`".

2.

Keeping track of the future statements a user has typed, so that later input gets compiled while those remain active.

Each of these capabilities — and a combined approach handling both — is offered by the `codeop` module.

For only the first of them:

 codeop.compile_command(*source*, *filename='&lt;input&gt;'*, *symbol='single'*)

Attempts to compile *source*, expected to be a string of Python code, returning a code object whenever *source* holds valid Python code. When that happens, the code object's filename attribute is set to *filename*, whose default value is `'<input>'`. The function returns `None` when *source* is *not* valid Python code yet forms a prefix of code that would be valid.

When something goes wrong with *source*, an exception gets raised. Invalid Python syntax triggers [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), while an invalid literal triggers [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

The *symbol* argument decides the compilation target: a statement (`'single'`, the default value), a sequence of [statement](https://docs.python.org/3.14/glossary.html#term-statement) (`'exec'`), or an [expression](https://docs.python.org/3.14/glossary.html#term-expression) (`'eval'`). Supplying any other value raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Note

There's a slim (though unlikely) chance that the parser concludes successfully before it has consumed the whole source; when that occurs, trailing symbols might be discarded rather than triggering an error. As an illustration, a backslash trailed by two newlines could be trailed by arbitrary garbage. A better parser API will eventually resolve this.

[Subject index](INDEX.md) · [Continue](codeop-compile-class.md)

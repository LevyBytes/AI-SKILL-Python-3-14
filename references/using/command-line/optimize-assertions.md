# -O

-O

Strip out assert statements along with any code that depends on the value of [`__debug__`](https://docs.python.org/3.14/library/constants.html#debug__). Extend the name of compiled ([bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode)) files by inserting `.opt-1` ahead of the `.pyc` extension (see [**PEP 488**](https://peps.python.org/pep-0488/)). See also `PYTHONOPTIMIZE`.

Changed in version 3.5: Modify `.pyc` filenames according to [**PEP 488**](https://peps.python.org/pep-0488/).

[Subject index](INDEX.md) · [Previous source section](isolated-mode.md) · [Following source section](remove-docstrings.md)

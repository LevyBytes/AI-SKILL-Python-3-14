# What’s New in Python 2.1 / PEP 207: Rich Comparisons

### PEP 207: Rich Comparisons

Earlier Python releases offered only rudimentary facilities for defining comparisons on user-defined classes and extension types. A class could supply a `__cmp__()` method that received two instances of the class and was limited to returning 0 when they matched or +1 or -1 when they didn’t; that method was barred from raising an exception or yielding anything besides a Boolean value. People working with Numeric Python frequently judged this scheme too restrictive and weak, since in the heavy number-crunching that numeric Python serves, being able to compare two matrices element by element — handing back a matrix that holds each element’s comparison result — would be far handier. And when the matrices differ in size, the comparison needs to raise an exception to flag the mistake.

Python 2.1 introduced rich comparisons to meet exactly this requirement. A Python class may now separately overload each of the `<`, `<=`, `>`, `>=`, `==`, and `!=` operations. Here are the new magic method names:

| Operation | Method name |
| --- | --- |
| `<` | `__lt__()` |
| `<=` | `__le__()` |
| `>` | `__gt__()` |
| `>=` | `__ge__()` |
| `==` | `__eq__()` |
| `!=` | `__ne__()` |

(These magic methods take their names from the matching Fortran operators `.LT.`. `.LE.`, &c. Programmers in the numeric world will almost surely recognize these labels at once and have little trouble recalling them.)

Every one of these magic methods follows the shape `method(self, other)`, in which `self` denotes the object sitting on the operator’s left side, while `other` denotes the one on its right side. As an example, evaluating the expression `A < B` results in `A.__lt__(B)` being invoked.

Each such magic method is free to hand back literally anything: a Boolean, a matrix, a list, or whatever other Python object you like. Or else they may raise an exception when the comparison turns out to be impossible, inconsistent, or otherwise without meaning.

The built-in `cmp(A,B)` function is able to draw on the rich comparison machinery, and it now takes an optional argument naming which comparison operation to apply; you supply this as one of the strings `"<"`, `"<="`, `">"`, `">="`, `"=="`, or `"!="`. When invoked without that optional third argument, `cmp()` keeps returning only -1, 0, or +1 just as in earlier Python releases; supply it, and it calls the right method and may hand back any Python object.

There are matching changes that will interest C programmers too; type objects gain a new slot `tp_richcmp`, plus an API for carrying out a specified rich comparison. Rather than detail the C API here, I’ll point you to [**PEP 207**](https://peps.python.org/pep-0207/), or to 2.1’s C API documentation, for the complete roster of related functions.

See also

[**PEP 207**](https://peps.python.org/pep-0207/) - Rich Comparisons

Authored and coded by Guido van Rossum, drawing substantially on prior groundwork from David Ascher.

[Subject index](INDEX.md) · [Previous source section](pep-236-future-directives.md) · [Next source section](pep-230-warning-framework.md) · [Release/subject declaration](introduction.md)

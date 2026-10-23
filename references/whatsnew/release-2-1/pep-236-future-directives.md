# What’s New in Python 2.1 / PEP 236: __future__ Directives - __future__

### PEP 236: __future__ Directives

Nested scopes provoked broad worry over the risk of the 2.1 release breaking existing code, and that worry ran deep enough to push the Pythoneers toward a more cautious stance. The plan is to establish a convention for switching on optional behavior in release N which then turns mandatory in release N+1.

The syntax leans on a `from...import` statement naming the reserved module [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__). You enable nested scopes with this statement:

```python
from __future__ import nested_scopes

```

Although it resembles an ordinary [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement, it isn’t one; tight rules govern where you may place such a future statement. They’re allowed only at the very top of a module, ahead of any Python code or normal `import` statements. The reason is that these statements can influence how the Python bytecode compiler reads code and produces bytecode, so they have to come before any statement that would emit bytecodes.

See also

[**PEP 236**](https://peps.python.org/pep-0236/) - Back to the [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__)

Written by Tim Peters, and primarily implemented by Jeremy Hylton.

[Subject index](INDEX.md) · [Previous source section](pep-227-nested-scopes.md) · [Next source section](pep-207-rich-comparisons.md) · [Release/subject declaration](introduction.md)

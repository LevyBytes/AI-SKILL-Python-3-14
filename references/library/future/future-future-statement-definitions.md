# __future__ — `__future__` — Future statement definitions

### `__future__` — Future statement definitions

**Source code:** [Lib/__future__.py](https://github.com/python/cpython/tree/3.14/Lib/__future__.py)

---

An import written as `from __future__ import feature` is known as a [future statement](https://docs.python.org/3.14/reference/simple_stmts.html#future). The Python compiler treats these specially so that a module carrying such a statement can adopt new Python capabilities ahead of the release where they turn into the default.

Even though the compiler attaches this extra meaning to future statements, they still run exactly like any ordinary import, and `__future__` itself is a real module that the import system manages just as it would any other Python module. Three goals motivate this approach:

- Keeping existing tools that scan import statements from getting confused when they look for the modules being imported.

- Recording the moment an incompatible change first appeared, together with the point at which it becomes — or already became — required. Because this acts as executable documentation, you can probe it from code by importing `__future__` and looking over what it holds.

- Guaranteeing that [future statements](https://docs.python.org/3.14/reference/simple_stmts.html#future) executed on releases older than Python 2.1 at the very least raise runtime errors — importing `__future__` there fails, since no module by that name existed before 2.1.

[Subject index](INDEX.md) · [Previous](future-statement-definitions.md) · [Continue](future-feature-class.md)

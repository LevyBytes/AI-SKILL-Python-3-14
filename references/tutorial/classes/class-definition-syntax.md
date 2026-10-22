# 9.3.1. Class Definition Syntax

### 9.3.1. Class Definition Syntax

The most basic shape a class definition can take is this:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

```

Class definitions, much like function definitions ([`def`](https://docs.python.org/3.14/reference/compound_stmts.html#def) statements), have to be run before they accomplish anything. (You could, in principle, tuck a class definition into one arm of an [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement, or set it inside a function.)

Realistically, the statements within a class definition tend to be function definitions, although other statements are permitted and are occasionally handy — we'll return to that point later. The function definitions sitting inside a class typically carry an odd-looking argument list, a shape demanded by the calling conventions methods follow — once more, this gets explained further on.

On entering a class definition, a fresh namespace is built and serves as the local scope — so every assignment to a local variable lands in this new namespace. Function definitions, in particular, bind the new function's name right here.

When a class definition finishes normally (by reaching its end), a *class object* results. It is, in essence, a wrapper enclosing the contents of the namespace that the class definition produced; we'll dig deeper into class objects in the following section. The local scope that was originally active (the one in force right before the class definition was entered) comes back, and the class object gets bound there under the class name declared in the class definition header (`ClassName` in the example).

[Subject index](INDEX.md) · [Previous source section](a-first-look-at-classes.md) · [Following source section](class-objects.md)

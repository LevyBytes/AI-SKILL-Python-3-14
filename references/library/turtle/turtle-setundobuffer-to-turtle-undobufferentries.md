# turtle: `turtle.setundobuffer()`, `turtle.undobufferentries()`

turtle.setundobuffer(*size*)

Parameters:

**size** – an integer or `None`

Assign or switch off the undobuffer. When *size* is an integer, a fresh empty undobuffer of that size is set up. *size* states how many turtle actions the `undo()` method/function can at most reverse. When *size* is `None`, the undobuffer is switched off.

```pycon
>>> turtle.setundobuffer(42)

```

 turtle.undobufferentries()

Hand back the count of entries held in the undobuffer.

```pycon
>>> while undobufferentries():
...     undo()

```

[Subject index](INDEX.md) · [Previous](turtle-poly-to-turtle-getscreen.md) · [Continue](compound-shapes.md) · [Owning module, declaration or section: Special Turtle methods](turtle-poly-to-turtle-getscreen.md)

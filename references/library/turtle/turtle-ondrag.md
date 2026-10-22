# turtle: `turtle.ondrag()`

turtle.ondrag(*fun*, *btn=1*, *add=None*)

Parameters:

- **fun** – a function taking two arguments, which will receive the coordinates of the point clicked on the canvas

- **btn** – number of the mouse-button, defaults to 1 (left mouse button)

- **add** – `True` or `False` – when `True`, an additional binding is registered; otherwise it supersedes an earlier binding

Attach *fun* to mouse-move events occurring on this turtle. When *fun* is `None`, present bindings get cleared.

Remark: a mouse-click event on a given turtle always comes before any run of mouse-move-events on that turtle.

```pycon
>>> turtle.ondrag(turtle.goto)

```

After that, clicking and dragging the Turtle moves it about the screen, leaving handdrawings behind (when the pen is down).

[Subject index](INDEX.md) · [Previous](turtle-onclick-to-turtle-onrelease.md) · [Continue](turtle-poly-to-turtle-getscreen.md) · [Owning module, declaration or section: Using events](turtle-onclick-to-turtle-onrelease.md)

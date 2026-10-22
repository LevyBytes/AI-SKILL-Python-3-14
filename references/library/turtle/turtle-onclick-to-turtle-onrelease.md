# turtle: `turtle.onclick()`, `turtle.onrelease()`

### Using events

 turtle.onclick(*fun*, *btn=1*, *add=None*)

Parameters:

- **fun** – a function taking two arguments, which will receive the coordinates of the point clicked on the canvas

- **btn** – number of the mouse-button, defaults to 1 (left mouse button)

- **add** – `True` or `False` – when `True`, an additional binding is registered; otherwise it supersedes an earlier binding

Attach *fun* to mouse-click events occurring on this turtle. When *fun* is `None`, present bindings get cleared. Here is an example using the anonymous turtle, i.e. the procedural style:

```pycon
>>> def turn(x, y):
...     left(180)
...
>>> onclick(turn)  # Now clicking into the turtle will turn it.
>>> onclick(None)  # event-binding will be removed

```

 turtle.onrelease(*fun*, *btn=1*, *add=None*)

Parameters:

- **fun** – a function taking two arguments, which will receive the coordinates of the point clicked on the canvas

- **btn** – number of the mouse-button, defaults to 1 (left mouse button)

- **add** – `True` or `False` – when `True`, an additional binding is registered; otherwise it supersedes an earlier binding

Attach *fun* to mouse-button-release events occurring on this turtle. When *fun* is `None`, present bindings get cleared.

```pycon
>>> class MyTurtle(Turtle):
...     def glow(self,x,y):
...         self.fillcolor("red")
...     def unglow(self,x,y):
...         self.fillcolor("")
...
>>> turtle = MyTurtle()
>>> turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
>>> turtle.onrelease(turtle.unglow) # releasing turns it to transparent.

```

[Subject index](INDEX.md) · [Previous](turtle-shapetransform-to-turtle-get-shapepoly.md) · [Continue](turtle-ondrag.md)

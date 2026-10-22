# turtle: `turtle.goto()`, `turtle.setpos()`, `turtle.setposition()`, `turtle.teleport()`

turtle.goto(*x*, *y=None*)

 turtle.setpos(*x*, *y=None*)

 turtle.setposition(*x*, *y=None*)

Parameters:

- **x** ? a number or a pair/vector of numbers

- **y** ? a number or `None`

When *y* is `None`, *x* has to be a coordinate pair or a `Vec2D` (such as what `pos()` hands back).

Relocate the turtle to an absolute spot. When the pen is down, a line is drawn. Leave the turtle's orientation unchanged.

```pycon
>>> tp = turtle.pos()
>>> tp
(0.00,0.00)
>>> turtle.setpos(60,30)
>>> turtle.pos()
(60.00,30.00)
>>> turtle.setpos((20,80))
>>> turtle.pos()
(20.00,80.00)
>>> turtle.setpos(tp)
>>> turtle.pos()
(0.00,0.00)

```

 turtle.teleport(*x*, *y=None*, ***, *fill_gap=False*)

Parameters:

- **x** ? a number or `None`

- **y** ? a number or `None`

- **fill_gap** ? a boolean

Relocate the turtle to an absolute spot. In contrast to goto(x, y), no line gets drawn. The orientation of the turtle stays the same. Should a fill be in progress, the polygon(s) departed from are filled upon leaving, with filling resuming once the teleport lands. Passing fill_gap=True turns this off, treating the phantom line crossed while teleporting as a fill boundary, just as goto(x, y) does.

```pycon
>>> tp = turtle.pos()
>>> tp
(0.00,0.00)
>>> turtle.teleport(60)
>>> turtle.pos()
(60.00,0.00)
>>> turtle.teleport(y=10)
>>> turtle.pos()
(60.00,10.00)
>>> turtle.teleport(20, 30)
>>> turtle.pos()
(20.00,30.00)

```

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](turtle-forward-to-turtle-lt.md) · [Continue](turtle-setx-to-turtle-home.md) · [Owning module, declaration or section: Turtle motion](turtle-forward-to-turtle-lt.md)

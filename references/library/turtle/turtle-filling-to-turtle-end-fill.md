# Filling

#### Filling

 turtle.filling()

Hand back the fillstate (`True` while filling, otherwise `False`).

```pycon
>>> turtle.begin_fill()
>>> if turtle.filling():
...    turtle.pensize(5)
... else:
...    turtle.pensize(3)

```

 turtle.fill()

Fill whatever shape is drawn within the `with turtle.fill():` block.

```pycon
>>> turtle.color("black", "red")
>>> with turtle.fill():
...     turtle.circle(80)

```

Calling `fill()` amounts to placing a `begin_fill()` ahead of the fill-block plus an `end_fill()` once the fill-block ends:

```pycon
>>> turtle.color("black", "red")
>>> turtle.begin_fill()
>>> turtle.circle(80)
>>> turtle.end_fill()

```

Added in version 3.14.

 turtle.begin_fill()

Invoke this right before you draw a shape that will be filled.

 turtle.end_fill()

Fill whatever shape was drawn since the most recent `begin_fill()` call.

Whether overlap regions belonging to self-intersecting polygons or to several shapes end up filled is governed by the operating system graphics, the kind of overlap, and how many overlaps occur. As an illustration, the Turtle star shown above could turn out entirely yellow or could contain some white regions.

```pycon
>>> turtle.color("black", "red")
>>> turtle.begin_fill()
>>> turtle.circle(80)
>>> turtle.end_fill()

```

[Subject index](INDEX.md) · [Previous](turtle-fillcolor-to-color.md) · [Continue](turtle-reset-to-turtle-write.md)

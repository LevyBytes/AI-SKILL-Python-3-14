# turtle: `turtle.circle()`, `turtle.dot()`, `turtle.stamp()`

turtle.circle(*radius*, *extent=None*, *steps=None*)

Parameters:

- **radius** ? a number

- **extent** ? a number (or `None`)

- **steps** ? an integer (or `None`)

Trace a circle of the supplied *radius*. Its center lies *radius* units to the left of the turtle; *extent* ? an angle ? sets how much of the circle gets drawn. With *extent* omitted, the full circle is drawn. When *extent* falls short of a full circle, the arc's starting endpoint is wherever the pen currently rests. The arc runs counterclockwise when *radius* is positive, and clockwise otherwise. At the end, the turtle's direction shifts by the size of *extent*.

Since an inscribed regular polygon stands in for the circle, *steps* fixes how many steps get used. Omit it and the value is worked out for you. This can serve to draw regular polygons.

```pycon
>>> turtle.home()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0
>>> turtle.circle(50)
>>> turtle.position()
(-0.00,0.00)
>>> turtle.heading()
0.0
>>> turtle.circle(120, 180)  # draw a semicircle
>>> turtle.position()
(0.00,240.00)
>>> turtle.heading()
180.0

```

 turtle.dot()

 turtle.dot(*size*)

 turtle.dot(*color*, */*)

 turtle.dot(*size*, *color*, */*)

 turtle.dot(*size*, *r*, *g*, *b*, */*)

Parameters:

- **size** ? an integer >= 1 (if given)

- **color** ? a colorstring or a numeric color tuple

Paint a round dot of diameter *size* in the given *color*. When *size* is left out, whichever is larger of `pensize+4` and `2*pensize` applies.

```pycon
>>> turtle.home()
>>> turtle.dot()
>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
>>> turtle.position()
(100.00,-0.00)
>>> turtle.heading()
0.0

```

 turtle.stamp()

Imprint a duplicate of the turtle's shape onto the canvas wherever the turtle currently sits. Hand back a stamp_id for that imprint, usable later to remove it via `clearstamp(stamp_id)`.

```pycon
>>> turtle.color("blue")
>>> stamp_id = turtle.stamp()
>>> turtle.fd(50)

```

[Subject index](INDEX.md) · [Previous](turtle-setx-to-turtle-home.md) · [Continue](turtle-clearstamp-to-turtle-undo.md) · [Owning module, declaration or section: Turtle motion](turtle-forward-to-turtle-lt.md)

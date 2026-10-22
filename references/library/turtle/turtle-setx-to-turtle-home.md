# turtle: `turtle.setx()`, `turtle.sety()`, `turtle.setheading()`, `turtle.seth()`, `turtle.home()`

turtle.setx(*x*)

Parameters:

**x** ? a number (integer or float)

Assign *x* as the turtle's first coordinate while keeping the second coordinate as it was.

```pycon
>>> turtle.position()
(0.00,240.00)
>>> turtle.setx(10)
>>> turtle.position()
(10.00,240.00)

```

 turtle.sety(*y*)

Parameters:

**y** ? a number (integer or float)

Assign *y* as the turtle's second coordinate while keeping the first coordinate as it was.

```pycon
>>> turtle.position()
(0.00,40.00)
>>> turtle.sety(-10)
>>> turtle.position()
(0.00,-10.00)

```

 turtle.setheading(*to_angle*)

 turtle.seth(*to_angle*)

Parameters:

**to_angle** ? a number (integer or float)

Point the turtle's orientation at *to_angle*. A few familiar directions, expressed in degrees, are these:

| standard mode | logo mode |
| --- | --- |
| 0 - east | 0 - north |
| 90 - north | 90 - east |
| 180 - west | 180 - south |
| 270 - south | 270 - west |

```pycon
>>> turtle.setheading(90)
>>> turtle.heading()
90.0

```

 turtle.home()

Send the turtle to the origin ? coordinates (0,0) ? and reset its heading to the start-orientation (which the mode determines, see `mode()`).

```pycon
>>> turtle.heading()
90.0
>>> turtle.position()
(0.00,-10.00)
>>> turtle.home()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0

```

[Subject index](INDEX.md) · [Previous](turtle-goto-to-turtle-teleport.md) · [Continue](turtle-circle-to-turtle-stamp.md) · [Owning module, declaration or section: Turtle motion](turtle-forward-to-turtle-lt.md)

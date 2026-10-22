# turtle: `turtle.pendown()`, `turtle.pd()`, `turtle.down()`, `turtle.penup()`, `turtle.pu()`, `turtle.up()`, `turtle.pensize()`, `turtle.width()`

### Pen control

#### Drawing state

 turtle.pendown()

 turtle.pd()

 turtle.down()

Lower the pen ? marks appear as the turtle moves.

 turtle.penup()

 turtle.pu()

 turtle.up()

Raise the pen ? no marks appear as the turtle moves.

 turtle.pensize(*width=None*)

 turtle.width(*width=None*)

Parameters:

**width** ? a positive number

Assign the line thickness to *width*, or read it back. Where resizemode equals ?auto? and the turtleshape is a polygon, that polygon gets rendered with this same line thickness. Call it with no argument and the present pensize comes back.

```pycon
>>> turtle.pensize()
1
>>> turtle.pensize(10)   # from here on lines of width 10 are drawn

```

[Subject index](INDEX.md) · [Continue](turtle-pen.md)

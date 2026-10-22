# turtle: `turtle.position()`, `turtle.pos()`, `turtle.towards()`, `turtle.xcor()`, `turtle.ycor()`, `turtle.heading()`

### Tell Turtle’s state

 turtle.position()

 turtle.pos()

Hand back where the turtle presently sits, (x,y), as a `Vec2D` vector.

```pycon
>>> turtle.pos()
(440.00,-0.00)

```

 turtle.towards(*x*, *y=None*)

Parameters:

- **x** ? a number, or a pair/vector made of numbers, or else an instance of a turtle

- **y** ? a number if *x* is a number, else `None`

Give the angle measured between the line running from the turtle to the spot named by (x,y), the vector, or the other turtle. The result rests on the turtle's start orientation, itself a function of the mode - ?standard?/?world? or ?logo?.

```pycon
>>> turtle.goto(10, 10)
>>> turtle.towards(0,0)
225.0

```

 turtle.xcor()

Hand back the turtle's x coordinate.

```pycon
>>> turtle.home()
>>> turtle.left(50)
>>> turtle.forward(100)
>>> turtle.pos()
(64.28,76.60)
>>> print(round(turtle.xcor(), 5))
64.27876

```

 turtle.ycor()

Hand back the turtle's y coordinate.

```pycon
>>> turtle.home()
>>> turtle.left(60)
>>> turtle.forward(100)
>>> print(turtle.pos())
(50.00,86.60)
>>> print(round(turtle.ycor(), 5))
86.60254

```

 turtle.heading()

Hand back the heading the turtle currently holds (the value hinges on the turtle mode, see `mode()`).

```pycon
>>> turtle.home()
>>> turtle.left(67)
>>> turtle.heading()
67.0

```

[Subject index](INDEX.md) · [Previous](turtle-speed.md) · [Continue](turtle-distance.md)

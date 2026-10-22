# turtle: `turtle.distance()`

turtle.distance(*x*, *y=None*)

Parameters:

- **x** ? a number, or a pair/vector made of numbers, or else an instance of a turtle

- **y** ? a number if *x* is a number, else `None`

Give the separation, in turtle step units, between the turtle and (x,y), the supplied vector, or the supplied other turtle.

```pycon
>>> turtle.home()
>>> turtle.distance(30,40)
50.0
>>> turtle.distance((30,40))
50.0
>>> joe = Turtle()
>>> joe.forward(77)
>>> turtle.distance(joe)
77.0

```

[Subject index](INDEX.md) · [Previous](turtle-position-to-turtle-heading.md) · [Continue](turtle-degrees-to-turtle-radians.md)

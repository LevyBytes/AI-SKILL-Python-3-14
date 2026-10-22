# Appearance: `turtle.shearfactor()`, `turtle.tilt()`, `turtle.tiltangle()`

turtle.shearfactor(*shear=None*)

Parameters:

**shear** – number (optional)

Assign or read the present shearfactor. Shear turtleshape by the supplied shearfactor shear, equal to the tangent of the shear angle. This leaves the turtle's heading (its direction of movement) untouched. When shear is omitted: hand back the present shearfactor, that is the tangent of the shear angle by which lines running parallel to the turtle's heading get sheared.

```pycon
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.shearfactor(0.5)
>>> turtle.shearfactor()
0.5

```

 turtle.tilt(*angle*)

Parameters:

**angle** – a number

Turn turtleshape by *angle* relative to its present tilt-angle, while leaving the turtle's heading (its direction of movement) untouched.

```pycon
>>> turtle.reset()
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.tilt(30)
>>> turtle.fd(50)
>>> turtle.tilt(30)
>>> turtle.fd(50)

```

 turtle.tiltangle(*angle=None*)

Parameters:

**angle** – a number (optional)

Assign or read the present tilt-angle. When angle is supplied, turn turtleshape to face the direction that angle names, no matter what its present tilt-angle is. This leaves the turtle's heading (its direction of movement) untouched. When angle is omitted: hand back the present tilt-angle, that is the angle separating the turtleshape's orientation from the turtle's heading (its direction of movement).

```pycon
>>> turtle.reset()
>>> turtle.shape("circle")
>>> turtle.shapesize(5,2)
>>> turtle.tilt(45)
>>> turtle.tiltangle()
45.0

```

[Subject index](INDEX.md) · [Previous](turtle-shape-to-turtle-turtlesize.md) · [Continue](turtle-shapetransform-to-turtle-get-shapepoly.md) · [Owning module, declaration or section: Appearance](turtle-shape-to-turtle-turtlesize.md)

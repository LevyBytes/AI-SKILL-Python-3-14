# Appearance: `turtle.shapetransform()`, `turtle.get_shapepoly()`

turtle.shapetransform(*t11=None*, *t12=None*, *t21=None*, *t22=None*)

Parameters:

- **t11** – a number (optional)

- **t12** – a number (optional)

- **t21** – a number (optional)

- **t12** – a number (optional)

Assign or read the turtle shape's present transformation matrix.

When no matrix element is supplied, hand back the transformation matrix as a 4-element tuple. Otherwise assign the supplied elements and transform turtleshape per the matrix whose first row holds t11, t12 and whose second row holds t21, t22. The determinant t11 * t22 - t12 * t21 has to be nonzero, or else an error is raised. Adjust stretchfactor, shearfactor and tiltangle per the supplied matrix.

```pycon
>>> turtle = Turtle()
>>> turtle.shape("square")
>>> turtle.shapesize(4,2)
>>> turtle.shearfactor(-0.5)
>>> turtle.shapetransform()
(4.0, -1.0, -0.0, 2.0)

```

 turtle.get_shapepoly()

Hand back the present shape polygon as a tuple of coordinate pairs. You can use this to build a fresh shape or pieces of a compound shape.

```pycon
>>> turtle.shape("square")
>>> turtle.shapetransform(4, -1, 0, 2)
>>> turtle.get_shapepoly()
((50, -20), (30, 20), (-50, 20), (-30, -20))

```

[Subject index](INDEX.md) · [Previous](turtle-shearfactor-to-turtle-tiltangle.md) · [Continue](turtle-onclick-to-turtle-onrelease.md) · [Owning module, declaration or section: Appearance](turtle-shape-to-turtle-turtlesize.md)

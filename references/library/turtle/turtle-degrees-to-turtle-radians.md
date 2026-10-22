# Settings for measurement

### Settings for measurement

 turtle.degrees(*fullcircle=360.0*)

Parameters:

**fullcircle** ? a number

Configure the units of angle measurement ? that is, how many ?degrees? make up a full circle. The default sits at 360 degrees.

```pycon
>>> turtle.home()
>>> turtle.left(90)
>>> turtle.heading()
90.0

>>> # Change angle measurement unit to grad (also known as gon,
>>> # grade, or gradian and equals 1/100-th of the right angle.)
>>> turtle.degrees(400.0)
>>> turtle.heading()
100.0
>>> turtle.degrees(360)
>>> turtle.heading()
90.0

```

 turtle.radians()

Switch the angle measurement units over to radians. The same as `degrees(2*math.pi)`.

```pycon
>>> turtle.home()
>>> turtle.left(90)
>>> turtle.heading()
90.0
>>> turtle.radians()
>>> turtle.heading()
1.5707963267948966

```

[Subject index](INDEX.md) · [Previous](turtle-distance.md) · [Continue](turtle-pendown-to-turtle-width.md)

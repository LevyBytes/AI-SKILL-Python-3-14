# turtle: `turtle.forward()`, `turtle.fd()`, `turtle.back()`, `turtle.bk()`, `turtle.backward()`, `turtle.right()`, `turtle.rt()`, `turtle.left()`, `turtle.lt()`

### Turtle motion

 turtle.forward(*distance*)

 turtle.fd(*distance*)

Parameters:

**distance** ? a number (integer or float)

Advance the turtle by the given *distance*, along whatever direction the turtle currently faces.

```pycon
>>> turtle.position()
(0.00,0.00)
>>> turtle.forward(25)
>>> turtle.position()
(25.00,0.00)
>>> turtle.forward(-75)
>>> turtle.position()
(-50.00,0.00)

```

 turtle.back(*distance*)

 turtle.bk(*distance*)

 turtle.backward(*distance*)

Parameters:

**distance** ? a number

Send the turtle backward by *distance*, the reverse of where the turtle faces. Leave the turtle's heading untouched.

```pycon
>>> turtle.position()
(0.00,0.00)
>>> turtle.backward(30)
>>> turtle.position()
(-30.00,0.00)

```

 turtle.right(*angle*)

 turtle.rt(*angle*)

Parameters:

**angle** ? a number (integer or float)

Rotate the turtle to the right by *angle* units. (By default those units are degrees, though the `degrees()` and `radians()` functions can change that.) How the angle is oriented hinges on the turtle mode, see `mode()`.

```pycon
>>> turtle.heading()
22.0
>>> turtle.right(45)
>>> turtle.heading()
337.0

```

 turtle.left(*angle*)

 turtle.lt(*angle*)

Parameters:

**angle** ? a number (integer or float)

Rotate the turtle to the left by *angle* units. (By default those units are degrees, though the `degrees()` and `radians()` functions can change that.) How the angle is oriented hinges on the turtle mode, see `mode()`.

```pycon
>>> turtle.heading()
22.0
>>> turtle.left(45)
>>> turtle.heading()
67.0

```

[Subject index](INDEX.md) · [Previous](methods-of-rawturtle-turtle-and-corresponding-functions.md) · [Continue](turtle-goto-to-turtle-teleport.md)

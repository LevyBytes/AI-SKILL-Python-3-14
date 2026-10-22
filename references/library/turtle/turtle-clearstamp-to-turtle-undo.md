# turtle: Stamp removal and turtle undo

turtle.clearstamp(*stampid*)

Parameters:

**stampid** ? an integer, must be return value of previous `stamp()` call

Remove the stamp carrying the given *stampid*.

```pycon
>>> turtle.position()
(150.00,-0.00)
>>> turtle.color("blue")
>>> astamp = turtle.stamp()
>>> turtle.fd(50)
>>> turtle.position()
(200.00,-0.00)
>>> turtle.clearstamp(astamp)
>>> turtle.position()
(200.00,-0.00)

```

 turtle.clearstamps(*n=None*)

Parameters:

**n** ? an integer (or `None`)

Remove all of the turtle's stamps, or the first/last *n* of them. With *n* set to `None`, every stamp goes; with *n* > 0 the first *n* stamps go; and with *n* < 0 the last *n* stamps go.

```pycon
>>> for i in range(8):
...     unused_stamp_id = turtle.stamp()
...     turtle.fd(30)
>>> turtle.clearstamps(2)
>>> turtle.clearstamps(-2)
>>> turtle.clearstamps()

```

 turtle.undo()

Reverse (over and over) the turtle's most recent action(s). How many undo actions remain available comes down to the undobuffer's size.

```pycon
>>> for i in range(4):
...     turtle.fd(50); turtle.lt(80)
...
>>> for i in range(8):
...     turtle.undo()

```

[Subject index](INDEX.md) · [Previous](turtle-circle-to-turtle-stamp.md) · [Continue](turtle-speed.md) · [Owning module, declaration or section: Turtle motion](turtle-forward-to-turtle-lt.md)

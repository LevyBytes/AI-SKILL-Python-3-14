# Explanation

### Explanation

A turtle object renders onto a screen object, and the turtle object-oriented interface holds several key classes you can use to construct these and tie them together.

Whenever a `Turtle` instance is made, it will build a `Screen` instance on its own if none yet exists.

`Turtle` derives from `RawTurtle`, which *doesn’t* generate a drawing surface for you - you must supply or make a *canvas* on its behalf. That *canvas* may be a `tkinter.Canvas`, `ScrolledCanvas` or `TurtleScreen`.

`TurtleScreen` is the fundamental drawing surface for a turtle. `Screen`, a subclass of `TurtleScreen`, brings along extra methods for handling its look (such as size and title) and its behaviour. The constructor of `TurtleScreen` requires a `tkinter.Canvas` or a `ScrolledCanvas` to be passed.

The functional interface for turtle graphics draws on the assorted methods of `Turtle` and `TurtleScreen`/`Screen`. Under the hood, a screen object springs into being any time a function derived from a `Screen` method runs. In the same way, a turtle object springs into being any time any function derived from a Turtle method runs.

For more than one turtle on a single screen, you must rely on the object-oriented interface.

[Subject index](INDEX.md) · [Previous](turtle-vec2d-class.md) · [Continue](how-to-use-help.md)

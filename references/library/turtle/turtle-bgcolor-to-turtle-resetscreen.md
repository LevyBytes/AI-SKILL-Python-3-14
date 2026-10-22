# turtle: `turtle.bgcolor()`, `bgcolor()`, `turtle.bgpic()`, `turtle.clear()`, `turtle.clearscreen()`, `turtle.reset()`, `turtle.resetscreen()`

### Window control

 turtle.bgcolor()

 turtle.bgcolor(*color*, */*)

 turtle.bgcolor(*r*, *g*, *b*, */*)

Read or assign the background color of the TurtleScreen.

The call accepts four distinct argument styles:

`bgcolor()`

Hand back the present background color as a color specification string or as a tuple (see the example). The result is suitable as an argument to a later color/pencolor/fillcolor/bgcolor call.

`bgcolor(colorstring)`

Assign the background color from *colorstring*, a Tk color specification string — for instance `"red"`, `"yellow"`, or `"#33cc8c"`.

`bgcolor((r, g, b))`

Assign the background color from the RGB color carried in the tuple of *r*, *g*, and *b*. Every one of *r*, *g*, and *b* has to fall within 0..colormode, where colormode equals either 1.0 or 255 (see `colormode()`).

`bgcolor(r, g, b)`

Assign the background color from the RGB color built out of *r*, *g*, and *b*. Every one of *r*, *g*, and *b* has to fall within 0..colormode.

```pycon
>>> screen.bgcolor("orange")
>>> screen.bgcolor()
'orange'
>>> screen.bgcolor("#800080")
>>> screen.bgcolor()
(128.0, 0.0, 128.0)

```

 turtle.bgpic(*picname=None*)

Parameters:

**picname** – a string giving the filename of an image (PNG, GIF, PGM, and PPM), or else `"nopic"`, or `None`

Assign a background image or hand back the name of the current backgroundimage. When *picname* is a filename, set that image as the background. When *picname* is `"nopic"`, remove the background image if one exists. When *picname* is `None`, hand back the filename of the current backgroundimage.

```python
>>> screen.bgpic()
'nopic'
>>> screen.bgpic("landscape.gif")
>>> screen.bgpic()
"landscape.gif"

```

 turtle.clear()

Note

This TurtleScreen method is reachable as a global function exclusively under the name `clearscreen`. The global function `clear` is a separate one, derived from the Turtle method `clear`.

 turtle.clearscreen()

Remove every drawing and every turtle from the TurtleScreen. Return the now-empty TurtleScreen to its starting state: white background, no background image, no event bindings, and tracing switched on.

 turtle.reset()

Note

This TurtleScreen method is reachable as a global function exclusively under the name `resetscreen`. The global function `reset` is a separate one, derived from the Turtle method `reset`.

 turtle.resetscreen()

Return every Turtle on the Screen to its starting state.

[Subject index](INDEX.md) · [Previous](methods-of-turtlescreen-screen-and-corresponding-functions.md) · [Continue](turtle-screensize-to-turtle-setworldcoordinates.md)

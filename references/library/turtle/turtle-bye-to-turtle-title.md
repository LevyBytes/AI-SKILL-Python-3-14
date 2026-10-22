# Methods specific to Screen, not inherited from TurtleScreen

### Methods specific to Screen, not inherited from TurtleScreen

 turtle.bye()

Close the turtlegraphics window.

 turtle.exitonclick()

Attach the `bye()` method to mouse clicks made on the Screen.

When the “using_IDLE” entry in the configuration dictionary is `False` (its default), mainloop is entered as well. Note: when IDLE runs with the `-n` switch (no subprocess), set this entry to `True` inside `turtle.cfg`. Under that arrangement, IDLE’s own mainloop also runs for the client script.

 turtle.save(*filename*, *overwrite=False*)

Write out the current turtle drawing (along with its turtles) as a PostScript file.

Parameters:

- **filename** – the path of the saved PostScript file

- **overwrite** – when `False`, should a file under the supplied filename already be present, the function raises a `FileExistsError`. When set to `True`, that existing file gets overwritten.

```pycon
>>> screen.save("my_drawing.ps")
>>> screen.save("my_drawing.ps", overwrite=True)

```

Added in version 3.14.

 turtle.setup(*width=_CFG['width']*, *height=_CFG['height']*, *startx=_CFG['leftright']*, *starty=_CFG['topbottom']*)

Establish the dimensions and placement of the main window. The defaults for the arguments live in the configuration dictionary and may be altered through a `turtle.cfg` file.

Parameters:

- **width** – an integer gives a pixel size, a float gives a fraction of the screen; the default equals 50% of screen

- **height** – an integer gives the pixel height, a float gives a fraction of the screen; the default equals 75% of screen

- **startx** – a positive value sets the starting pixel position from the screen’s left edge, a negative one measures from the right edge, and `None` centers the window horizontally

- **starty** – a positive value sets the starting pixel position from the screen’s top edge, a negative one measures from the bottom edge, and `None` centers the window vertically

```pycon
>>> screen.setup (width=200, height=200, startx=0, starty=0)
>>>              # sets window to 200x200 pixels, in upper left of screen
>>> screen.setup(width=.75, height=0.5, startx=None, starty=None)
>>>              # sets window to 75% of screen by 50% of screen and centers

```

 turtle.title(*titlestring*)

Parameters:

**titlestring** – a string displayed within the titlebar of the window for turtle graphics

Assign *titlestring* as the title of the turtle window.

```pycon
>>> screen.title("Welcome to the turtle zoo!")

```

[Subject index](INDEX.md) · [Previous](turtle-register-shape-to-turtle-window-width.md) · [Continue](turtle-rawturtle-class-to-turtle-rawpen-class.md)

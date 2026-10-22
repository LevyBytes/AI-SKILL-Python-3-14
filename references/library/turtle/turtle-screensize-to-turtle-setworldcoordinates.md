# turtle: `turtle.screensize()`, `turtle.setworldcoordinates()`

turtle.screensize(*canvwidth=None*, *canvheight=None*, *bg=None*)

Parameters:

- **canvwidth** – positive integer, new width of canvas in pixels

- **canvheight** – positive integer, new height of canvas in pixels

- **bg** – colorstring or color-tuple, new background color

When called with no arguments, hand back the current (canvaswidth, canvasheight). Otherwise resize the canvas on which the turtles draw. The drawing window itself stays unchanged. To view hidden portions of the canvas, rely on the scrollbars. By this means you can bring into view those portions of a drawing that previously lay beyond the canvas.

```python
>>> screen.screensize()
(400, 300)
>>> screen.screensize(2000,1500)
>>> screen.screensize()
(2000, 1500)

```

e.g. to search for an erroneously escaped turtle ;-)

 turtle.setworldcoordinates(*llx*, *lly*, *urx*, *ury*)

Parameters:

- **llx** – a number, x-coordinate of lower left corner of canvas

- **lly** – a number, y-coordinate of lower left corner of canvas

- **urx** – a number, x-coordinate of upper right corner of canvas

- **ury** – a number, y-coordinate of upper right corner of canvas

Establish a user-defined coordinate system and shift into mode “world” when needed. Doing so triggers a `screen.reset()`. When mode “world” is already in effect, every drawing is redrawn to match the new coordinates.

**ATTENTION**: within user-defined coordinate systems angles can look distorted.

```pycon
>>> screen.reset()
>>> screen.setworldcoordinates(-50,-7.5,50,7.5)
>>> for _ in range(72):
...     left(10)
...
>>> for _ in range(8):
...     left(45); fd(2)   # a regular octagon

```

[Subject index](INDEX.md) · [Previous](turtle-bgcolor-to-turtle-resetscreen.md) · [Continue](turtle-no-animation-to-turtle-update.md) · [Owning module, declaration or section: Window control](turtle-bgcolor-to-turtle-resetscreen.md)

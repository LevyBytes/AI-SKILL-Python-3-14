# How to configure Screen and Turtles

### How to configure Screen and Turtles

The built-in default configuration imitates the look and behaviour of the old turtle module so as to keep compatibility with it as high as possible.

Should you prefer a different configuration that better captures this module’s features or that suits your own purposes better, e.g. for classroom use, you can set up a configuration file `turtle.cfg` that gets read at import time and adjusts the configuration per its settings.

The built in configuration is equivalent to the following `turtle.cfg`:

```ini
width = 0.5
height = 0.75
leftright = None
topbottom = None
canvwidth = 400
canvheight = 300
mode = standard
colormode = 1.0
delay = 10
undobuffersize = 1000
shape = classic
pencolor = black
fillcolor = black
resizemode = noresize
visible = True
language = english
exampleturtle = turtle
examplescreen = screen
title = Python Turtle Graphics
using_IDLE = False

```

Brief notes on a few of the entries:

- The opening four lines map to the arguments of the `Screen.setup` method.

- Lines 5 and 6 map to the arguments of the `Screen.screensize` method.

- *shape* may be any built-in shape, e.g: arrow, turtle, etc. For further detail, try `help(shape)`.

- To use no fill color at all (i.e. render the turtle transparent), put `fillcolor = ""` (but every nonempty string in the cfg file must omit quotes).

- To have the turtle mirror its state, set `resizemode = auto`.

- When you set, say, `language = italian`, the docstringdict `turtle_docstringdict_italian.py` is loaded at import time (provided it sits on the import path, e.g. in the same directory as `turtle`).

- The *exampleturtle* and *examplescreen* entries name these objects as they appear within the docstrings. Converting method-docstrings into function-docstrings strips these names out of the docstrings.

- *using_IDLE*: Turn this to `True` if you routinely use IDLE together with its `-n` switch (“no subprocess”). Doing so keeps `exitonclick()` from entering the mainloop.

You may place one `turtle.cfg` file in the directory holding `turtle` and another one in the current working directory. The second will take precedence over the settings of the first.

Inside the `Lib/turtledemo` directory sits a `turtle.cfg` file. You can examine it as a sample and observe its effects while running the demos (ideally not from inside the demo-viewer).

[Subject index](INDEX.md) · [Previous](turtle-write-docstringdict.md) · [Continue](../turtledemo/turtledemo-demo-scripts.md)

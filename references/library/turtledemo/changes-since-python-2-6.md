# turtledemo — Changes since Python 2.6

### Changes since Python 2.6

- The methods `Turtle.tracer`, `Turtle.window_width` and `Turtle.window_height` are gone. Methods bearing these names and functionality now live solely as methods of `Screen`. The functions derived from them are still around. (Indeed, even back in Python 2.6 these methods just duplicated the matching `TurtleScreen`/`Screen` methods.)

- The `Turtle.fill()` method is gone. The behaviour of `begin_fill()` and `end_fill()` shifted a little: every filling operation must now finish with an `end_fill()` call.

- A `Turtle.filling` method has been introduced. It hands back a boolean: `True` while a filling operation is ongoing, `False` if not. This mirrors a `fill()` call given no arguments in Python 2.6.

[Subject index](INDEX.md) · [Previous](turtledemo-demo-scripts.md) · [Continue](changes-since-python-3-0.md) · [Owning module, declaration or section: turtledemo](turtledemo-demo-scripts.md)

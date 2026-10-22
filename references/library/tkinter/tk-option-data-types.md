# tkinter — Tk Option Data Types

### Tk Option Data Types

anchor

The permitted values are compass points: `"n"`, `"ne"`, `"e"`, `"se"`, `"s"`, `"sw"`, `"w"`, `"nw"`, plus `"center"`.

bitmap

Eight named bitmaps come built in: `'error'`, `'gray25'`, `'gray50'`, `'hourglass'`, `'info'`, `'questhead'`, `'question'`, `'warning'`. To name an X bitmap file instead, supply the file’s full path with an `@` in front, as in `"@/usr/contrib/bitmap/gumby.bit"`.

boolean

Acceptable here are the integers 0 or 1, or else the strings `"yes"` or `"no"`.

callback

Any Python function taking no arguments will do. As an example:

```python
def print_it():
    print("hi there")
fred["command"] = print_it

```

color

You may state colors either by the X color names found in the rgb.txt file, or as strings holding RGB values across 4 bit: `"#RGB"`, 8 bit: `"#RRGGBB"`, 12 bit: `"#RRRGGGBBB"`, or 16 bit: `"#RRRRGGGGBBBB"` ranges, where each R,G,B stands for any valid hex digit. Page 160 of Ousterhout’s book has the particulars.

cursor

You can use the standard X cursor names out of `cursorfont.h`, dropping the `XC_` prefix. For a hand cursor (`XC_hand2`), say, pass the string `"hand2"`. Supplying your own bitmap and mask file is also an option. Consult page 179 of Ousterhout’s book.

distance

Screen distances may be expressed either in pixels or as absolute distances. Pixels come through as numbers, while absolute distances arrive as strings whose final character marks the unit: `c` for centimetres, `i` for inches, `m` for millimetres, `p` for printer’s points. Thus 3.5 inches is written `"3.5i"`.

font

Tk works with a list font name format, like `{courier 10 bold}`. A positive font-size number is read as points; a negative one is read as pixels.

geometry

This is a string shaped `widthxheight`, where, for most widgets, width and height are counted in pixels (in characters for widgets that show text). For example: `fred["geometry"] = "200x100"`.

justify

The permitted values are the strings `"left"`, `"center"`, and `"right"`.

region

This is a string of four space-separated elements, each one a valid distance (per above). For instance, `"2 3 4 5"`, `"3i 2i 4.5i 2i"`, and `"3c 2c 4c 10.43c"` all count as valid regions.

relief

Sets which border style a widget takes on. The permitted values are `"raised"`, `"sunken"`, `"flat"`, `"groove"`, and `"ridge"`.

scrollcommand

Nearly always this is the `set()` method belonging to some scrollbar widget, though it may be any widget method that accepts one argument.

wrap

It has to be one of `"none"`, `"char"`, or `"word"`.

[Subject index](INDEX.md) · [Previous](the-window-manager.md) · [Continue](bindings-and-events.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)

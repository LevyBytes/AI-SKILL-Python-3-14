# tkinter.font — `tkinter.font` — Tkinter font wrapper

## tkinter.font — Tkinter font wrapper

### `tkinter.font` — Tkinter font wrapper

**Source code:** [Lib/tkinter/font.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/font.py)

---

For building and working with named fonts, the `tkinter.font` module offers the `Font` class.

Here are the available font weights and slants:

 tkinter.font.NORMAL

 tkinter.font.BOLD

 tkinter.font.ITALIC

 tkinter.font.ROMAN

 *class *tkinter.font.Font(*root=None*, *font=None*, *name=None*, *exists=False*, ***options*)

A named font is represented by the `Font` class. Each *Font* instance carries a unique name and may be described through its family, size, and style configuration. Named fonts are how Tk creates and refers to a font as one object, instead of restating a font's attributes everywhere it appears.

>

arguments:

>   *font* - font specifier tuple (family, size, options) *name* - unique font name *exists* - self points to existing named font if true

extra keyword options (disregarded when *font* is supplied):

>   *family* - font family i.e. Courier, Times *size* - font size  If *size* is positive it is interpreted as size in points. If *size* is a negative number its absolute value is treated as size in pixels.  *weight* - font emphasis (NORMAL, BOLD) *slant* - ROMAN, ITALIC *underline* - font underlining (0 - none, 1 - underline) *overstrike* - font strikeout (0 - none, 1 - strikeout)

 actual(*option=None*, *displayof=None*)

Give back the font's attributes.

 cget(*option*)

Fetch a single attribute of the font.

 config(***options*)

Modify attributes of the font.

 copy()

Hand back a fresh instance of the present font.

 measure(*text*, *displayof=None*)

Give the amount of room the text would take up on the named display when laid out in the current font. With no display named, the program's main window is assumed.

 metrics(**options*, ***kw*)

Return font-specific data. Options include:

*ascent* - distance between baseline and highest point that a

character of the font can occupy

*descent* - distance between baseline and lowest point that a

character of the font can occupy

*linespace* - minimum vertical separation necessary between any two

characters of the font such that no two lines overlap vertically.

*fixed* - 1 if font is fixed-width else 0

 tkinter.font.families(*root=None*, *displayof=None*)

Return the different font families.

 tkinter.font.names(*root=None*)

Give back the names of the fonts that are defined.

 tkinter.font.nametofont(*name*, *root=None*)

Hand back a `Font` representation of a tk named font.

Changed in version 3.10: The *root* parameter was added.

[Subject index](INDEX.md)

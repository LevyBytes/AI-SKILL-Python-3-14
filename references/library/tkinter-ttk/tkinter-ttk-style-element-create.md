# tkinter.ttk.Style: `element_create()`

element_create(*elementname*, *etype*, **args*, ***kw*)

Within the current theme, build a fresh element whose *etype* should be one of "image", "from" or "vsapi". That last one only exists in Tk 8.6 on Windows.

When "image" is the choice, *args* should hold the default image name followed by statespec/value pairs (which forms the imagespec), and *kw* may carry the following options:

border=padding

Here padding is a list holding up to four integers that give the left, top, right, and bottom borders in turn.

height=height

Sets a smallest height for the element. Whenever the value drops below zero, the height of the base image serves as the default.

padding=padding

Sets the interior padding of the element. When unset, it falls back to border's value.

sticky=spec

Governs where the image sits inside the final parcel. spec holds zero or more of the characters "n", "s", "w", or "e".

width=width

Sets a smallest width for the element. Whenever the value drops below zero, the width of the base image serves as the default.

Example:

```python
img1 = tkinter.PhotoImage(master=root, file='button.png')
img1 = tkinter.PhotoImage(master=root, file='button-pressed.png')
img1 = tkinter.PhotoImage(master=root, file='button-active.png')
style = ttk.Style(root)
style.element_create('Button.button', 'image',
                     img1, ('pressed', img2), ('active', img3),
                     border=(2, 4), sticky='we')

```

When "from" is the value handed to *etype*, `element_create()` will clone an existing element. *args* should hold a themename, the source from which the element gets cloned, and optionally an element to clone from. When this element to clone from is left out, an empty element is used instead. *kw* is discarded.

Example:

```python
style = ttk.Style(root)
style.element_create('plain.background', 'from', 'default')

```

When "vsapi" is the value handed to *etype*, `element_create()` adds a fresh element to the active theme whose on-screen look is drawn by way of the Microsoft Visual Styles API, the component behind the themed styles on Windows XP and Vista. *args* should hold the Visual Styles class and part as listed in the Microsoft documentation, followed by an optional sequence of tuples pairing ttk states with the matching Visual Styles API state value. *kw* may carry the following options:

padding=padding

Sets the interior padding of the element. *padding* is a list holding up to four integers that give the left, top, right and bottom padding amounts in turn. Should fewer than four entries appear, bottom falls back to top, right falls back to left, and top falls back to left. Put differently, three numbers cover the left, vertical, and right padding; two numbers cover the horizontal and the vertical padding; one number applies the same padding around every side of the widget. No other options may accompany this one.

margins=padding

Sets the exterior padding of the elements. *padding* is a list holding up to four integers that give the left, top, right and bottom padding amounts in turn. No other options may accompany this one.

width=width

Sets the width for the element. With this option in place, the Visual Styles API is not consulted for the recommended size of the part. With this option in place, *height* ought to be set as well. Mixing the *width* and *height* options together with the *padding* or *margins* options is not permitted.

height=height

Sets the height of the element. Refer to the notes given for *width*.

Example:

```python
style = ttk.Style(root)
style.element_create('pin', 'vsapi', 'EXPLORERBAR', 3, [
                     ('pressed', '!selected', 3),
                     ('active', '!selected', 2),
                     ('pressed', 'selected', 6),
                     ('active', 'selected', 5),
                     ('selected', 4),
                     ('', 1)])
style.layout('Explorer.Pin',
             [('Explorer.Pin.pin', {'sticky': 'news'})])
pin = ttk.Checkbutton(style='Explorer.Pin')
pin.pack(expand=True, fill='both')

```

Changed in version 3.13: Added support of the "vsapi" element factory.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-style-layout.md) · [Continue](ttk-style-elements-and-theme-selection.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Style](tkinter-ttk-style-class.md) · [Owning module, declaration or section: Ttk Styling](tkinter-ttk-style-class.md)

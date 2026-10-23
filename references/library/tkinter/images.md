# tkinter - Images

### Images

You build images of the various formats by going through the matching `tkinter.Image` subclass:

- `BitmapImage` handles images held in XBM format.

- `PhotoImage` handles images held in PGM, PPM, GIF and PNG formats. Support for that last one arrived with Tk 8.6.

You create either kind of image through the `file` option or the `data` option (further options exist too).

Changed in version 3.13: Introduced the `PhotoImage` method `copy_replace()`, which lifts a region from one image into another and can optionally zoom or subsample at the pixel level. A *from_coords* parameter now joins the `PhotoImage` methods `copy()`, `zoom()` and `subsample()`. The *zoom* together with *subsample* parameters now join the `PhotoImage` method `copy()`.

From there the image object serves anywhere some widget honors an `image` option (labels, buttons, menus, for instance). In such spots Tk holds no reference of its own to the image. Once the final Python reference to the image object goes away, the image data goes with it, and Tk shows an empty box at every place the image had been used.

See also

The [Pillow](https://python-pillow.org/) package brings in support for further formats, BMP, JPEG, TIFF, and WebP among them.

[Subject index](INDEX.md) · [Previous](the-index-parameter.md) · [Continue](widget-tk-createfilehandler-to-tkinter-exception.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)

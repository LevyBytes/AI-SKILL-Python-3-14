# tkinter.scrolledtext: `tkinter.scrolledtext.ScrolledText`

## tkinter.scrolledtext — Scrolled Text Widget

### `tkinter.scrolledtext` — Scrolled Text Widget

**Source code:** [Lib/tkinter/scrolledtext.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/scrolledtext.py)

---

The `tkinter.scrolledtext` module ships a like-named class that realizes a plain text widget paired with a vertical scroll bar wired up to behave sensibly. Reaching for the `ScrolledText` class spares you the trouble of wiring a text widget and a scroll bar together by hand.

Inside a `Frame`, the text widget and the scrollbar are packed side by side, and the `Grid` and `Pack` geometry-manager methods are pulled in from that `Frame` object. Because of this, the `ScrolledText` widget can be used on its own to handle most everyday geometry management.

If you need finer control, you can rely on these attributes:

 *class *tkinter.scrolledtext.ScrolledText(*master=None*, ***kw*)

 frame

The frame wrapping around the text widget and the scroll bar.

[Subject index](INDEX.md) · [Continue](tkinter-scrolledtext-scrolled-text-widget.md)

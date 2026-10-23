# What's New In Python 3.13 / tkinter - tkinter, tkinter.ttk

### tkinter

- New [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) widget methods have arrived: `tk_busy_hold()`, `tk_busy_configure()`, `tk_busy_cget()`, `tk_busy_forget()`, `tk_busy_current()`, and `tk_busy_status()`. (Contributed by Miguel, klappnase and Serhiy Storchaka in [gh-72684](https://github.com/python/cpython/issues/72684).)

- The [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) widget's `wm_attributes()` method now takes an attribute name lacking the minus prefix when fetching window attributes ? for instance `w.wm_attributes('alpha')` ? and permits passing attribute/value pairs as keyword arguments to set them, such as `w.wm_attributes(alpha=0.5)`. (Contributed by Serhiy Storchaka in [gh-43457](https://github.com/python/cpython/issues/43457).)

- By way of the new optional keyword-only parameter *return_python_dict*, `wm_attributes()` is able to deliver attributes inside a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). (Contributed by Serhiy Storchaka in [gh-43457](https://github.com/python/cpython/issues/43457).)

- With the new optional keyword-only parameter *return_ints*, `Text.count()` is able to give back a plain [`int`](https://docs.python.org/3.14/library/functions.html#int). Without it, that lone count comes as a 1-tuple or `None`. (Contributed by Serhiy Storchaka in [gh-97928](https://github.com/python/cpython/issues/97928).)

- The ?vsapi? element type is now supported within the [`element_create()`](https://docs.python.org/3.14/library/tkinter.ttk.html#tkinter.ttk.Style.element_create) method of [`tkinter.ttk.Style`](https://docs.python.org/3.14/library/tkinter.ttk.html#tkinter.ttk.Style). (Contributed by Serhiy Storchaka in [gh-68166](https://github.com/python/cpython/issues/68166).)

- An `after_info()` method has been added for Tkinter widgets. (Contributed by Cheryl Sabella in [gh-77020](https://github.com/python/cpython/issues/77020).)

- A new `copy_replace()` method on `PhotoImage` copies a region out of one image into another, optionally applying pixel zooming, subsampling, or both. (Contributed by Serhiy Storchaka in [gh-118225](https://github.com/python/cpython/issues/118225).)

- A *from_coords* parameter has been added to the `PhotoImage` methods `copy()`, `zoom()` and `subsample()`. The `PhotoImage` method `copy()` also gains *zoom* and *subsample* parameters. (Contributed by Serhiy Storchaka in [gh-118225](https://github.com/python/cpython/issues/118225).)

- The `PhotoImage` object gains a `read()` method to load an image from a file and a `data()` method to retrieve the image data. Its `write()` method picks up *background* and *grayscale* parameters. (Contributed by Serhiy Storchaka in [gh-118271](https://github.com/python/cpython/issues/118271).)

[Subject index](INDEX.md) · [Previous source section](time.md) · [Next source section](traceback.md) · [Release/subject declaration](summary-release-highlights.md)

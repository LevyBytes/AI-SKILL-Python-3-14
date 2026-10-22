# turtle: `turtle.textinput()`, `turtle.numinput()`

### Input methods

 turtle.textinput(*title*, *prompt*)

Parameters:

- **title** – string

- **prompt** – string

Open a dialog window prompting for a string of input. The title parameter sets the dialog window's title, while prompt is text that generally explains which information to enter. Hand back the entered string. Should the dialog be canceled, hand back `None`.

```python
>>> screen.textinput("NIM", "Name of first player:")

```

 turtle.numinput(*title*, *prompt*, *default=None*, *minval=None*, *maxval=None*)

Parameters:

- **title** – string

- **prompt** – string

- **default** – number (optional)

- **minval** – number (optional)

- **maxval** – number (optional)

[Subject index](INDEX.md) · [Previous](turtle-onclick-to-turtle-done.md) · [Required continuation of the source contract](input-methods.md)

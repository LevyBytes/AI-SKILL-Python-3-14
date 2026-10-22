# turtle: Numeric input dialogs and value bounds

Open a dialog box that asks for a numeric value. The title argument labels the dialog window, while prompt is text that typically explains which numeric value is wanted. default: a starting value, minval: the lowest acceptable input, maxval: the highest acceptable input. When minval and maxval are supplied, the entered number is constrained to lie between them. Otherwise, a hint appears and the dialog stays open until corrected. The entered number is returned. Should the dialog be canceled, `None` comes back.

```python
>>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

```

[Subject index](INDEX.md) · [Continue](turtle-mode-to-turtle-getshapes.md) · [Owning module, declaration or section: Input methods](turtle-textinput-to-turtle-numinput.md) · [Owning module, declaration or section: turtle.numinput](turtle-textinput-to-turtle-numinput.md) · [Preceding source contract and version conditions](turtle-textinput-to-turtle-numinput.md)

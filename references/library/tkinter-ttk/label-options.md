# tkinter.ttk — Label Options

### Label Options

Labels, buttons and other button-like widgets back the options below.

| Option | Description |
| --- | --- |
| text | Gives a text string to show inside the widget. |
| textvariable | Gives a name whose value stands in for the text option resource. |
| underline | When set, gives the index (0-based) of a character within the text string to underline. That underlined character drives mnemonic activation. |
| image | Gives an image to show. The value is a list of 1 or more elements. Its first element is the default image name. The remainder of the list, if present, is a series of statespec/value pairs per `Style.map()`, naming alternate images for when the widget sits in a given state or mix of states. Every image in the list ought to share the same size. |
| compound | Governs where the image sits relative to the text when both the text and images options are supplied. Permitted values: - text: show text alone - image: show image alone - top, bottom, left, right: place the image above, below, to the left of, or to the right of the text, in that order. - none: the default. show the image when one is present, else the text. |
| width | When above zero, fixes how much room, measured in character widths, is reserved for the text label; when below zero, fixes a minimum width. When zero or left unset, the text label's natural width applies. |

[Subject index](INDEX.md) · [Previous](scrollable-widget-options.md) · [Continue](compatibility-options.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)

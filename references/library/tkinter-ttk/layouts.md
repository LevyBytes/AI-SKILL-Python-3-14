# tkinter.ttk — Layouts

### Layouts

A layout may be simply `None`, when it carries no options, or a dict of options stating how the element should be arranged. The layout mechanism leans on a stripped-down version of the pack geometry manager: starting from an initial cavity, each element receives a parcel.

The valid options/values are:

*side*: whichside

States which side of the cavity the element goes on; one of top, right, bottom or left. When left out, the element fills the whole cavity.

*sticky*: nswe

States where within its allocated parcel the element is positioned.

*unit*: 0 or 1

When set to 1, the element together with all of its descendants is treated as a single element for the purposes of `Widget.identify()` et al. This serves things such as scrollbar thumbs with grips.

*children*: [sublayout… ]

States a list of elements to position inside the element. Every entry takes the shape of a tuple (or another sequence type) whose first member is the layout name, while the remaining member is a Layout.

[Subject index](INDEX.md) · [Previous](ttk-style-elements-and-theme-selection.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)

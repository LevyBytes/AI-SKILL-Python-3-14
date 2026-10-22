# tkinter — The index Parameter

### The index Parameter

Quite a few widgets expect you to supply “index” parameters. They serve to pinpoint a spot within a Text widget, particular characters inside an Entry widget, or particular menu items in a Menu widget.

Entry widget indexes (index, view index, etc.)

Entry widgets carry options that point at character positions within the text on display. The following `tkinter` functions let you reach these special spots in text widgets:

Text widget indexes

For Text widgets the index notation is extremely rich, and the Tk man pages describe it best.

Menu indexes (menu.invoke(), menu.entryconfig(), etc.)

A number of menu options and methods act on specific menu entries. Whenever an option or parameter calls for a menu index, you may supply:

- an integer naming the entry’s numeric slot in the widget, tallied downward from the top beginning at 0;

- the string `"active"`, pointing to the menu slot the cursor is over right now;

- the string `"last"`, pointing to the final menu item;

- an integer with `@` in front, like `@6`, the integer being read as a y pixel coordinate within the menu’s own coordinate system;

- the string `"none"`, standing for no menu entry whatsoever, most commonly paired with menu.activate() to switch off every entry, and lastly,

- a text string that gets pattern-matched against the menu entry’s label, working from the top of the menu down. Bear in mind this index type is weighed only after all the rest, so entries labelled `last`, `active`, or `none` risk being taken as the literals above instead.

[Subject index](INDEX.md) · [Previous](bindings-and-events.md) · [Continue](images.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)

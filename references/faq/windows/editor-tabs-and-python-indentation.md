# How do I keep editors from inserting tabs into my Python source?

### How do I keep editors from inserting tabs into my Python source?

Tabs are something the FAQ advises against, and the Python style guide, [**PEP 8**](https://peps.python.org/pep-0008/), calls for 4 spaces in Python code meant for distribution; that figure is likewise the Emacs python-mode default.

No matter the editor, blending tabs with spaces is a poor choice. MSVC is no exception here, yet it is readily set to use spaces: go to Tools ‣ Options ‣ Tabs, then for the “Default” file type set “Tab size” along with “Indent size” to 4 and pick the “Insert spaces” radio button.

Whenever a blend of tabs and spaces is creating trouble in leading whitespace, Python throws [`IndentationError`](https://docs.python.org/3.14/library/exceptions.html#IndentationError) or [`TabError`](https://docs.python.org/3.14/library/exceptions.html#TabError). You can additionally invoke the [`tabnanny`](https://docs.python.org/3.14/library/tabnanny.html#module-tabnanny) module to scan a directory tree in batch mode.

[Subject index](INDEX.md)

# Format menu (Editor window only)

### Format menu (Editor window only)

Format Paragraph

Rewrap the text block holding the text insert cursor. Steer clear of code lines. Refer to Format block within the Editing and Navigation section that follows.

Indent Region

Shift selected lines right by the indent width (default 4 spaces).

Dedent Region

Shift selected lines left by the indent width (default 4 spaces).

Comment Out Region

Insert ## in front of selected lines.

Uncomment Region

Remove leading # or ## from selected lines.

Tabify Region

Convert *leading* runs of spaces to tabs. (Note: 4 space blocks are recommended for indenting Python code.)

Untabify Region

Convert *every* tab to the right number of spaces.

Toggle Tabs

Open a dialog to switch between indenting with spaces and tabs.

New Indent Width

Open a dialog for altering the indent width. The Python community’s accepted default is 4 spaces.

Strip Trailing Whitespace

Strip trailing spaces and other whitespace following the final non-whitespace character on a line by running [`str.rstrip()`](https://docs.python.org/3.14/library/stdtypes.html#str.rstrip) over every line, multiline strings included. Outside of Shell windows, also drop surplus newlines at the file’s end.

[Subject index](INDEX.md) · [Previous](edit-menu-shell-and-editor.md) · [Continue](run-menu-editor-window-only.md)

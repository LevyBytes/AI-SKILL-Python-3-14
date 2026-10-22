# Key bindings

### Key bindings

IDLE’s insertion cursor appears as a slim vertical bar sitting between character positions. As characters are typed, the insertion cursor and all text to its right shift right by one character while the new character fills the freed space.

A number of non-character keys reposition the cursor and may erase characters. Erasing does not put text onto the clipboard, though IDLE keeps an undo list. Anywhere this document mentions keys, ‘C’ denotes — under Windows and Unix — the Control key, and under macOS the Command key. (Every such mention presumes the keys were not re-bound to something different.)

- Arrow keys shift the cursor by a single character or line.

- C-LeftArrow and C-RightArrow shift one word leftward or rightward.

- Home and End jump to a line’s start or finish.

- Page Up and Page Down scroll a screenful up or down.

- C-Home and C-End jump to the file’s start or finish.

- Backspace and Del (or C-d) erase the character before or after.

- C-Backspace and C-Del remove a whole word to the left or right.

- C-k deletes (‘kills’) everything to the right.

Common keybindings (such as C-c for copy and C-v for paste) may function. The Configure IDLE dialog is where keybindings are chosen.

[Subject index](INDEX.md) · [Previous](editor-windows.md) · [Continue](automatic-indentation.md)

# curses.textpad.Textbox: `edit()`, `do_command()`, `gather()`

edit([*validator*])

For everyday use this is your way in. It takes in editing keystrokes right up until one of the termination keystrokes arrives. Pass a *validator* and it has to be a function; that function runs once per keystroke entered, receiving the keystroke as its parameter, and command dispatch keys off whatever it returns. What comes back from this method is the window contents as a string, with the `stripspaces` attribute governing whether blanks in the window count.

 do_command(*ch*)

Handle one command keystroke at a time. The special keystrokes it understands are listed here:

| Keystroke | Action |
| --- | --- |
| Control-A | Jump to the window's left edge. |
| Control-B | Move the cursor left, rolling onto the prior line where that fits. |
| Control-D | Remove the character beneath the cursor. |
| Control-E | Jump to the right edge (stripspaces off) or to the line's end (stripspaces on). |
| Control-F | Move the cursor right, rolling onto the next line where that fits. |
| Control-G | Finish up and return the window's contents. |
| Control-H | Erase the character behind the cursor. |
| Control-J | Finish if the window spans 1 line; otherwise add a newline. |
| Control-K | Drop the line when it is blank, else wipe through to the line's end. |
| Control-L | Redraw the screen. |
| Control-N | Cursor down; drop one line lower. |
| Control-O | Drop a blank line in at the cursor. |
| Control-P | Cursor up; rise one line higher. |

A move operation simply has no effect when the cursor already rests at an edge that blocks it. Wherever feasible, the synonyms below are honored:

| Constant | Keystroke |
| --- | --- |
| `KEY_LEFT` | Control-B |
| `KEY_RIGHT` | Control-F |
| `KEY_UP` | Control-P |
| `KEY_DOWN` | Control-N |
| `KEY_BACKSPACE` | Control-h |

Every remaining keystroke is read as an instruction to drop in that character and advance the cursor rightward (line wrapping included).

 gather()

Hand back the window contents as a string, where the `stripspaces` member dictates whether blanks in the window are counted.

 stripspaces

A flag, this attribute decides how blanks in the window get read. Switch it on and trailing blanks on every line are disregarded; any cursor movement that would otherwise settle on a trailing blank instead jumps to that line’s end, and trailing blanks fall away once the window contents are gathered.

[Subject index](INDEX.md) · [Previous](curses-textpad-textbox-class.md) · [Owning module, declaration or section: curses.textpad](curses-textpad-rectangle.md) · [Owning module, declaration or section: curses.textpad.Textbox](curses-textpad-textbox-class.md) · [Owning module, declaration or section: Textbox objects](curses-textpad-textbox-class.md)

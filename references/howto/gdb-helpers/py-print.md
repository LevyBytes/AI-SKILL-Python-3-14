# `py-print`

### `py-print`

>

The `py-print` command resolves a Python name and attempts to display it. Its search runs through locals in the current thread, next globals, and at last builtins:

```none
(gdb) py-print self
local 'self' = <SwappableArea(running=<gtk.Dialog at remote 0x98faaa4>,
main_page=0) at remote 0x98fa6e4>
(gdb) py-print __name__
global '__name__' = 'gnome_sudoku.dialog_swallower'
(gdb) py-print len
builtin 'len' = <built-in function len>
(gdb) py-print scarlet_pimpernel
'scarlet_pimpernel' not found

```

Where the current C frame maps to several Python frames, only the first is taken into account by `py-print`.

[Subject index](INDEX.md) · [Previous source context](py-bt.md) · [Following source context](py-locals.md)

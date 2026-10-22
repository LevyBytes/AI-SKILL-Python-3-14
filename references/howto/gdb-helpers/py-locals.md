# `py-locals`

### `py-locals`

>

The `py-locals` command gathers every Python local inside the current Python frame in the chosen thread and prints their representations:

```none
(gdb) py-locals
self = <SwappableArea(running=<gtk.Dialog at remote 0x98faaa4>,
main_page=0) at remote 0x98fa6e4>
d = <gtk.Dialog at remote 0x98faaa4>

```

Where the current C frame maps to several Python frames, locals drawn from all of them appear:

```none
(gdb) py-locals
Locals for recursive_function
n = 0
Locals for recursive_function
n = 1
Locals for recursive_function
n = 2
Locals for recursive_function
n = 3
Locals for recursive_function
n = 4
Locals for recursive_function
n = 5
Locals for <module>

```

[Subject index](INDEX.md) · [Previous source context](py-print.md) · [Following source context](use-with-gdb-commands.md)

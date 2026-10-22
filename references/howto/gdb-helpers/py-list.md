# `py-list`

### `py-list`

>

A `py-list` command comes with the extension; it shows the Python source code (when there is any) for the current frame in the chosen thread. A “>” marks the current line:

```none
(gdb) py-list
 901        if options.profile:
 902            options.profile = False
 903            profile_me()
 904            return
 905
>906        u = UI()
 907        if not u.quit:
 908            try:
 909                gtk.main()
 910            except KeyboardInterrupt:
 911                # properly quit on a keyboard interrupt...

```

Run `py-list START` to begin listing at another line number inside the Python source, and `py-list START,END` to list a particular span of lines inside the Python source.

[Subject index](INDEX.md) · [Previous source context](distinguishing-python-integers-strings-from-gdb-native-values.md) · [Following source context](py-up-and-py-down.md)

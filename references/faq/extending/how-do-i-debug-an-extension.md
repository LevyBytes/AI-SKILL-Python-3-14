# How do I debug an extension?

### How do I debug an extension?

If you run GDB against extensions that load dynamically, no breakpoint can be placed within your extension before that extension has actually been loaded.

Inside your `.gdbinit` file — or right there at the prompt — drop in the command:

```none
br _PyImport_LoadDynamicModule

```

After that, once you launch GDB:

```shell
$ gdb /local/bin/python
gdb) run myscript.py
gdb) continue # repeat until your extension is loaded
gdb) finish   # so that your extension is loaded
gdb) br myfunction.c:50
gdb) continue

```

[Subject index](INDEX.md)

# 16.1.2. Executable Python Scripts

### 16.1.2. Executable Python Scripts

Across BSD-style Unix platforms, you can turn a Python script into something runnable on its own, much like a shell script, by placing the line

```python
#!/usr/bin/env python3

```

(presuming the interpreter sits somewhere on the user’s `PATH`) at the very top of the file and then marking the file executable. Those two opening characters, `#!`, have to be the first two bytes of the file. Certain systems require that this opening line terminate with a Unix newline (`'\n'`) rather than the Windows variant (`'\r\n'`). Keep in mind that the hash (also called pound) symbol, `'#'`, marks the start of a comment in Python.

You grant the file its executable mode, or permission, by running the **chmod** command.

```shell
$ chmod +x myscript.py

```

Windows has no concept of an “executable mode”. Its Python installer wires up `.py` files to `python.exe`, so double-clicking a Python file launches it as a script. You may instead use the `.pyw` extension, which hides the console window that would otherwise pop up.

[Subject index](INDEX.md) · [Previous source section](error-handling.md) · [Following source section](the-interactive-startup-file.md)

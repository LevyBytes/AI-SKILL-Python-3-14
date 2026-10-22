# 2.4. Miscellaneous

### 2.4. Miscellaneous

For convenient use of Python scripts under Unix, give them the executable bit, for instance via

```shell
$ chmod +x script

```

and add a fitting Shebang line as the script's first line. One dependable pick is normally

```sh
#!/usr/bin/env python3

```

which hunts for the Python interpreter across the entire `PATH`. Some Unices, though, lack the **env** command, so you might have to write `/usr/bin/python3` directly as the interpreter path.

When you want to run shell commands from inside Python scripts, turn to the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module.

[Subject index](INDEX.md) · [Previous source section](python-related-paths-and-files.md) · [Following source section](custom-openssl.md)

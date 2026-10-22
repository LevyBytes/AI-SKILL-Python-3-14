# How do I make a Python script executable on Unix?

### How do I make a Python script executable on Unix?

Two steps are required: set the script file's mode to executable, and start the first line with `#!` followed by the path to the Python interpreter.

For the first, run `chmod +x scriptfile` or alternatively `chmod 755 scriptfile`.

The second has several variants. The simplest approach is to put

```python
#!/usr/local/bin/python

```

at the top of your file as its very first line, substituting the pathname where Python is installed on your platform.

To keep the script from depending on a fixed location for the Python interpreter, you can rely on the **env** program. Provided the Python interpreter sits in a directory on the user's `PATH`, nearly every Unix variant supports the following:

```python
#!/usr/bin/env python

```

*Don't* do this for CGI scripts. For CGI scripts the `PATH` variable is frequently stripped down, so you must spell out the interpreter's full absolute pathname.

Now and then a user's environment becomes so crowded that the **/usr/bin/env** program fails, or no env program exists at all. For those cases, you can fall back on the following hack (credited to Alex Rezinsky):

```sh
#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""

```

The small downside is that this sets the script's __doc__ string. You can correct that, however, by appending

```python
__doc__ = """...Whatever..."""

```

[Subject index](INDEX.md)

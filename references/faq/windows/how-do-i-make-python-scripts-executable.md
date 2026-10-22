# How do I make Python scripts executable?

### How do I make Python scripts executable?

Under Windows, the stock Python installer ties the .py extension to a file type (Python.File) and equips that file type with an open command that launches the interpreter (`D:\Program Files\Python\python.exe "%1" %*`). That alone lets you run scripts from the command prompt as ‘foo.py’. Should you prefer to fire off the script by simply entering ‘foo’ without any extension, you have to append .py to the PATHEXT environment variable.

[Subject index](INDEX.md)

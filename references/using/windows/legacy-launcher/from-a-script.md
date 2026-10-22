# 4.12.1.3. From a script

#### 4.12.1.3. From a script

Let's put together a test Python script - make a file named `hello.py` holding the contents below

```python
#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))

```

Out of the directory where hello.py resides, run the command:

```none
py hello.py

```

You ought to see the version number of your most recent Python 2.x install printed. Now try editing the first line so it reads:

```python
#! python3

```

Running the command again should now print details of the most recent Python 3.x. Just as with the command-line examples above, you may give a more specific version qualifier. Supposing you have Python 3.7 installed, try editing the first line to `#! python3.7` and you should see the 3.7 version details printed.

Note that, unlike interactive use, a plain "python" selects the most recent Python 2.x you have installed. That is for the sake of backward compatibility and of agreement with Unix, where the `python` command usually points at Python 2.

[Subject index](INDEX.md) · [Previous source section](virtual-environments.md) · [Following source section](from-file-associations.md)

# 16.1.3. The Interactive Startup File

### 16.1.3. The Interactive Startup File

During interactive Python sessions, it is often convenient to run a fixed set of commands automatically whenever the interpreter launches. Achieve this by pointing the environment variable [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) at a file holding those start-up commands. The idea mirrors the `.profile` mechanism found in Unix shells.

Python consults this file solely during interactive sessions; it skips it when reading commands from a script and when `/dev/tty` is named outright as the command source (even though that case otherwise acts interactive). The file runs within the very namespace your interactive commands use, which means whatever it defines or imports is reachable unqualified throughout the session. This is also where you can reassign the `sys.ps1` and `sys.ps2` prompts.

Should you also want to pull in a second start-up file from the working directory, code that into the global start-up file with something such as `if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())`. And if a script needs the startup file, you have to invoke it deliberately within that script:

```python
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)

```

[Subject index](INDEX.md) · [Previous source section](executable-python-scripts.md) · [Following source section](the-customization-modules.md)

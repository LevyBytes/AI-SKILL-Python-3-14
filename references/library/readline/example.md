# readline — Example

### Example

The example below shows how, with the `readline` module's history reading and writing functions, you can automatically pull in and persist a history file (named `.python_history`) sitting in the home directory of the user. Ordinarily the code below would run by itself during interactive sessions from the user's [`PYTHONSTARTUP`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSTARTUP) file.

```python
import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
    # default history len is -1 (infinite), which may grow unruly
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)

```

This code in fact runs automatically whenever Python launches in [interactive mode](https://docs.python.org/3.14/tutorial/interpreter.html#tut-interactive) (refer to [Readline configuration](https://docs.python.org/3.14/library/site.html#rlcompleter-config)).

The next example reaches the same end but accommodates concurrent interactive sessions, because it appends only the fresh history.

```python
import atexit
import os
import readline
histfile = os.path.join(os.path.expanduser("~"), ".python_history")

try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(histfile, 'wb').close()
    h_len = 0

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)
atexit.register(save, h_len, histfile)

```

The next example builds on the [`code.InteractiveConsole`](https://docs.python.org/3.14/library/code.html#code.InteractiveConsole) class to add history save/restore.

```python
import atexit
import code
import os
import readline

class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except FileNotFoundError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(1000)
        readline.write_history_file(histfile)

```

Note

readline is not supported by the new [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) that arrived in version 3.13. That said, you can still bring readline back into play by setting the [`PYTHON_BASIC_REPL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_BASIC_REPL) environment variable.

[Subject index](INDEX.md) · [Previous](readline-completion-and-display-hooks.md) · [Continue](../removed/removed-standard-library-modules.md) · [Owning module, declaration or section: readline](readline-backend.md)

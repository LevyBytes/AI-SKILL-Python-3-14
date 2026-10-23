# rlcompleter: `rlcompleter.Completer`

## rlcompleter - Completion function for GNU readline

### `rlcompleter` - Completion function for GNU readline

**Source code:** [Lib/rlcompleter.py](https://github.com/python/cpython/tree/3.14/Lib/rlcompleter.py)

---

The `rlcompleter` module supplies a completion function fit to be handed to [`set_completer()`](https://docs.python.org/3.14/library/readline.html#readline.set_completer) within the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module.

Whenever this module is imported on a Unix platform that has the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module on hand, an instance of the `Completer` class springs into being automatically and its `complete()` method is wired up as the [readline completer](https://docs.python.org/3.14/library/readline.html#readline-completion). That method delivers completion of valid Python [identifiers and keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers).

Example:

```python
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.

```

The `rlcompleter` module is meant to be used alongside Python's [interactive mode](https://docs.python.org/3.14/tutorial/interpreter.html#tut-interactive). So long as Python is not launched with the [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) option, the module gets imported and set up on its own (consult [Readline configuration](https://docs.python.org/3.14/library/site.html#rlcompleter-config)).

On platforms lacking [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline), the `Completer` class this module defines remains usable for purposes of your own.

 *class *rlcompleter.Completer

Completer objects have the following method:

[Subject index](INDEX.md) · [Continue](rlcompleter-completer-complete.md)

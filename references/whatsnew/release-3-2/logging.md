# What's New In Python 3.2 / logging - logging, logging.handlers, string, sys

### logging

Beyond the dictionary-driven configuration covered above, numerous further enhancements arrived in the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) package.

Three new documents now accompany the logging docs: a [basic tutorial](https://docs.python.org/3.14/howto/logging.html#logging-basic-tutorial), an [advanced tutorial](https://docs.python.org/3.14/howto/logging.html#logging-advanced-tutorial), and a [cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html#logging-cookbook) full of logging recipes. Reading them is the quickest route to understanding logging.

A *style* argument was added to the [`logging.basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) setup function so that three flavors of string formatting are selectable. Its default of ?%? keeps the classic %-formatting; switching to ?{? enables the newer [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) approach; and ?$? turns on the shell-style substitution that [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template) offers. Each of the three setups below produces the same effect:

```python
>>> from logging import basicConfig
>>> basicConfig(style='%', format="%(name)s -> %(levelname)s: %(message)s")
>>> basicConfig(style='{', format="{name} -> {levelname} {message}")
>>> basicConfig(style='$', format="$name -> $levelname: $message")

```

Should a logging event fire while no configuration exists yet, a fallback configuration now kicks in: a [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) aimed at [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) for any event at `WARNING` severity or above. Previously, an event raised ahead of any configuration would either throw an exception or quietly vanish, depending on what [`logging.raiseExceptions`](https://docs.python.org/3.14/library/logging.html#logging.raiseExceptions) was set to. This fresh fallback handler is kept in [`logging.lastResort`](https://docs.python.org/3.14/library/logging.html#logging.lastResort).

Working with filters got easier too. Rather than building a [`Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) object, you may now hand in any Python callable whose result is `True` or `False`.

Several additional refinements broaden flexibility and ease configuration. The module docs enumerate every change landing in Python 3.2.

[Subject index](INDEX.md) · [Previous source section](reprlib.md) · [Next source section](csv.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

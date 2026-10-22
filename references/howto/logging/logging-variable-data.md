# Logging variable data

### Logging variable data

When logging variable data, supply a format string as the event description message and pass the variable data afterward as arguments. As an example:

```python
import logging
logging.warning('%s before you %s', 'Look', 'leap!')

```

will display:

```none
WARNING:root:Look before you leap!

```

You'll notice that folding variable data into the event description message relies on the old %-style of string formatting. The reason is backwards compatibility: the logging package came before the more recent formatting alternatives such as [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) and [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template). Those newer formatting alternatives *are* supported, but examining them lies beyond what this tutorial covers: refer to [Using particular formatting styles throughout your application](https://docs.python.org/3.14/howto/logging-cookbook.html#formatting-styles) for further detail.

[Subject index](INDEX.md) · [Previous source context](logging-to-a-file.md) · [Following source context](changing-the-format-of-displayed-messages.md)

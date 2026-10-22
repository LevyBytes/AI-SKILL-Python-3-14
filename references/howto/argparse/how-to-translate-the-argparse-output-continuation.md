# How to translate the argparse output continuation

```shell
$ python prog.py --help
usage: prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

options:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet

```

Each of the strings `usage:`, `positional arguments:`, `options:` and `show this help message and exit` can be translated.

Before any of these strings can be translated, you have to pull them out into a `.po` file. As an illustration, with [Babel](https://babel.pocoo.org/) you would run this command:

```shell
$ pybabel extract -o messages.po /usr/lib/python3.12/argparse.py

```

Running it gathers every translatable string out of the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module and writes them to a file called `messages.po`. It takes for granted that your Python installation lives in `/usr/lib`.

To discover where the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module sits on your own machine, use this short script:

```python
import argparse
print(argparse.__file__)

```

After the entries in the `.po` file have been translated and those translations put in place with [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext), [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) becomes capable of showing the translated text.

When you want your own strings in the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) output translated, reach for [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext).

[Subject index](INDEX.md) · [Previous source owning section](how-to-translate-the-argparse-output.md) · [Following source context](custom-type-converters.md)

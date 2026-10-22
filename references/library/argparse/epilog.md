# argparse — epilog

### epilog

Certain programs prefer to print extra description of the program below the description of the arguments. You can give such text through the `epilog=` argument to `ArgumentParser`:

```python
>>> parser = argparse.ArgumentParser(
...     description='A foo that bars',
...     epilog="And that's how you'd foo a bar")
>>> parser.print_help()
usage: argparse.py [-h]

A foo that bars

options:
 -h, --help  show this help message and exit

And that's how you'd foo a bar

```

Just like the description argument, the `epilog=` text gets line-wrapped by default, though that behavior can be tuned with the formatter_class argument to `ArgumentParser`.

[Subject index](INDEX.md) · [Previous](description.md) · [Continue](parents.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

# argparse — Argument abbreviations (prefix matching)

### Argument abbreviations (prefix matching)

Out of the box, `parse_args()` lets a long option be shortened to a prefix as long as that prefix is unambiguous (it lines up with exactly one option):

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-bacon')
>>> parser.add_argument('-badger')
>>> parser.parse_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
>>> parser.parse_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
>>> parser.parse_args('-ba BA'.split())
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon

```

Any argument capable of matching several options raises an error. Turn this behavior off by setting allow_abbrev to `False`.

[Subject index](INDEX.md) · [Previous](arguments-containing.md) · [Continue](beyond-sys-argv.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

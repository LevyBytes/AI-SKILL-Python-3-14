# argparse - prefix_chars

### prefix_chars

The prefix on most command-line options is `-`, for example `-f/--foo`. Parsers that have to accommodate other or extra prefix characters — say, to permit options such as `+f` or `/foo` — can declare them through the `prefix_chars=` argument of the `ArgumentParser` constructor:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
>>> parser.add_argument('+f')
>>> parser.add_argument('++bar')
>>> parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')

```

`'-'` is the default for the `prefix_chars=` argument. Handing over a character set that leaves out `-` makes `-f/--foo` options impossible to use.

[Subject index](INDEX.md) · [Previous](formatter-class-code-example-parser-argparse-argumentparser.md) · [Continue](fromfile-prefix-chars.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

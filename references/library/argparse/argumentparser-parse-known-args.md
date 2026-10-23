# argparse - Partial parsing

### Partial parsing

 ArgumentParser.parse_known_args(*args=None*, *namespace=None*)

There are times when a script cares about only a particular subset of the command-line arguments and wants to hand off anything it does not recognize to some other script or program. The `parse_known_args()` method earns its keep in those situations.

Its behaviour mirrors `parse_args()`, except that surplus, unrecognized arguments never trigger an error. It simply parses the arguments it does know and gives back a two-item tuple: the filled-in namespace paired with the list of whatever it could not recognize.

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('bar')
>>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
(Namespace(bar='BAR', foo=True), ['--badger', 'spam'])

```

Warning

Prefix-matching rules are in force for `parse_known_args()`. Rather than passing such a token through to the leftover-arguments list, the parser can swallow an option when it is merely a prefix of some option it already knows.

[Subject index](INDEX.md) · [Previous](argumentparser-print-usage-to-argumentparser-format-help.md) · [Continue](argumentparser-convert-arg-line-to-args.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

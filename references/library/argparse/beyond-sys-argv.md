# argparse - Beyond `sys.argv`

### Beyond `sys.argv`

On occasion it helps to let an `ArgumentParser` work over arguments that don't come from [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv). You do this by handing a list of strings to `parse_args()`, which comes in handy when experimenting at the interactive prompt:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument(
...     'integers', metavar='int', type=int, choices=range(10),
...     nargs='+', help='an integer in the range 0..9')
>>> parser.add_argument(
...     '--sum', dest='accumulate', action='store_const', const=sum,
...     default=max, help='sum the integers (default: find the max)')
>>> parser.parse_args(['1', '2', '3', '4'])
Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
>>> parser.parse_args(['1', '2', '3', '4', '--sum'])
Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])

```

[Subject index](INDEX.md) · [Previous](argument-abbreviations-prefix-matching.md) · [Continue](argparse-namespace-class.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

# argparse — required

### required

By and large, the `argparse` module treats flags such as `-f` and `--bar` as marking *optional* arguments, the kind that may always be skipped on the command line. To turn an option into a *required* one, pass `True` for the `required=` keyword argument of `add_argument()`:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', required=True)
>>> parser.parse_args(['--foo', 'BAR'])
Namespace(foo='BAR')
>>> parser.parse_args([])
usage: [-h] --foo FOO
: error: the following arguments are required: --foo

```

As this example demonstrates, when an option carries `required`, `parse_args()` raises an error should that option be absent from the command line.

Note

Required options are usually regarded as poor practice, because users count on *options* being *optional*, so you should steer clear of them where you can.

[Subject index](INDEX.md) · [Previous](choices.md) · [Continue](help.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

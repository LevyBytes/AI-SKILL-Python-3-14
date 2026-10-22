# optparse — Callback example 3: check option order (generalized)

### Callback example 3: check option order (generalized)

Should you wish to reuse this callback across several similar options (set a flag, but blow up if `-b` already appeared), it requires a little effort: both the error message and the flag it sets have to be generalized.

```python
def check_order(option, opt_str, value, parser):
    if parser.values.b:
        raise OptionValueError("can't use %s after -b" % opt_str)
    setattr(parser.values, option.dest, 1)
...
parser.add_option("-a", action="callback", callback=check_order, dest='a')
parser.add_option("-b", action="store_true", dest="b")
parser.add_option("-c", action="callback", callback=check_order, dest='c')

```

[Subject index](INDEX.md) · [Previous](callback-example-2-check-option-order.md) · [Continue](callback-example-4-check-arbitrary-condition.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

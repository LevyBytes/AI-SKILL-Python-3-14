# optparse - Callback example 2: check option order

### Callback example 2: check option order

Here's a marginally more interesting example: note that `-a` appeared, but blow up if it shows up after `-b` along the command-line.

```python
def check_order(option, opt_str, value, parser):
    if parser.values.b:
        raise OptionValueError("can't use -a after -b")
    parser.values.a = 1
...
parser.add_option("-a", action="callback", callback=check_order)
parser.add_option("-b", action="store_true", dest="b")

```

[Subject index](INDEX.md) · [Previous](callback-example-1-trivial-callback.md) · [Continue](callback-example-3-check-option-order-generalized.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

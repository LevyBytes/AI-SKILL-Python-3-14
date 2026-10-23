# optparse - Callback example 4: check arbitrary condition

### Callback example 4: check arbitrary condition

Naturally, you can drop any condition in there—you aren't restricted to checking the values of options already defined. For instance, if you have options that ought not to be called when the moon is full, here's all you do:

```python
def check_moon(option, opt_str, value, parser):
    if is_moon_full():
        raise OptionValueError("%s option invalid when moon is full"
                               % opt_str)
    setattr(parser.values, option.dest, 1)
...
parser.add_option("--foo",
                  action="callback", callback=check_moon, dest="foo")

```

(Working out the definition of `is_moon_full()` is left as an exercise for the reader.)

[Subject index](INDEX.md) · [Previous](callback-example-3-check-option-order-generalized.md) · [Continue](callback-example-5-fixed-arguments.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

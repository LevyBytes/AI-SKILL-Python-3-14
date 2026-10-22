# optparse — Callback example 5: fixed arguments

### Callback example 5: fixed arguments

Matters grow a bit more interesting once you define callback options that take a fixed count of arguments. Declaring that a callback option takes arguments resembles defining a `"store"` or `"append"` option: define `type` and the option takes one argument that must be convertible to that type; further define `nargs` and the option takes `nargs` arguments.

Here's an example that simply mimics the standard `"store"` action:

```python
def store_value(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value)
...
parser.add_option("--foo",
                  action="callback", callback=store_value,
                  type="int", nargs=3, dest="foo")

```

Observe that `optparse` handles consuming 3 arguments and converting them into integers for you; your only job is to store them. (Or whatever; clearly you don't actually need a callback for this example.)

[Subject index](INDEX.md) · [Previous](callback-example-4-check-arbitrary-condition.md) · [Continue](callback-example-6-variable-arguments.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

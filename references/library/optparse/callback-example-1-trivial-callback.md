# optparse — Callback example 1: trivial callback

### Callback example 1: trivial callback

Below is an example of a callback option that takes no arguments and merely notes that the option appeared:

```python
def record_foo_seen(option, opt_str, value, parser):
    parser.values.saw_foo = True

parser.add_option("--foo", action="callback", callback=record_foo_seen)

```

Naturally, you could accomplish that with the `"store_true"` action.

[Subject index](INDEX.md) · [Previous](raising-errors-in-a-callback.md) · [Continue](callback-example-2-check-option-order.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

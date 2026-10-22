# optparse — Callback example 6: variable arguments

### Callback example 6: variable arguments

Things turn hairy once you want an option to take a variable count of arguments. For that scenario you have to write a callback, since `optparse` offers no built-in support for it. And you have to grapple with certain subtleties of conventional Unix command-line parsing that `optparse` usually takes care of on your behalf. Specifically, callbacks should honor the conventional rules for bare `--` and `-` arguments:

- either `--` or `-` can be option arguments

- a bare `--` (when it isn't serving as some option's argument): stop processing the command line and throw the `--` away

- a bare `-` (when it isn't serving as some option's argument): stop processing the command line yet retain the `-` (tack it onto `parser.largs`)

When you want an option that takes a variable count of arguments, several subtle, tricky matters demand attention. Which exact implementation you settle on will hinge on the trade-offs you're prepared to make for your application (which is precisely why `optparse` doesn't support this kind of thing directly).

Even so, here's an attempt at a callback for an option carrying variable arguments:

```python
def vararg_callback(option, opt_str, value, parser):
    assert value is None
    value = []

    def floatable(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    for arg in parser.rargs:
        # stop on --foo like options
        if arg[:2] == "--" and len(arg) > 2:
            break
        # stop on -a, but not on -3 or -3.0
        if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
            break
        value.append(arg)

    del parser.rargs[:len(value)]
    setattr(parser.values, option.dest, value)

...
parser.add_option("-c", "--callback", dest="vararg_attr",
                  action="callback", callback=vararg_callback)

```

[Subject index](INDEX.md) · [Previous](callback-example-5-fixed-arguments.md) · [Continue](extending-optparse.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

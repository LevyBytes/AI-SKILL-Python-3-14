# optparse - Default values

### Default values

Every one of the examples above sets some variable (the "destination") whenever certain command-line options appear. What happens when those options never appear? Since we supplied no defaults, they all come out `None`. Usually that's fine, yet now and then you crave tighter control. `optparse` permits a default value per destination, applied ahead of the command line being parsed.

First, take the verbose/quiet example. If we want `optparse` to set `verbose` to `True` unless `-q` shows up, then we can do this:

```python
parser.add_option("-v", action="store_true", dest="verbose", default=True)
parser.add_option("-q", action="store_false", dest="verbose")

```

Because default values attach to the *destination* rather than to any one option, and these two options happen to share a destination, this is precisely equivalent:

```python
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-q", action="store_false", dest="verbose", default=True)

```

Consider this:

```python
parser.add_option("-v", action="store_true", dest="verbose", default=False)
parser.add_option("-q", action="store_false", dest="verbose", default=True)

```

Once more, the default value for `verbose` will be `True`: for any given destination, the last default value supplied is the one that counts.

A tidier way to specify default values is OptionParser's `set_defaults()` method, callable any time before you call `parse_args()`:

```python
parser.set_defaults(verbose=True)
parser.add_option(...)
(options, args) = parser.parse_args()

```

As before, for a given option destination the last value specified is the one that counts. For clarity, stick to one method or the other of setting default values, not both.

[Subject index](INDEX.md) · [Previous](other-actions.md) · [Continue](generating-help.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

# optparse: `OptionParser.add_option()`

### Defining options

A single Option instance covers a group of synonymous command-line option strings, for example `-f` and `--file`. You're free to give as many short or long option strings as you want, provided at least one option string is present in total.

The standard way to build an `Option` instance is through the `add_option()` method on `OptionParser`.

 OptionParser.add_option(*option*)

 OptionParser.add_option(**opt_str*, *attr=value*, *...*)

To define an option with only a short option string:

```python
parser.add_option("-f", attr=value, ...)

```

And to define an option with only a long option string:

```python
parser.add_option("--foo", attr=value, ...)

```

The keyword arguments set up the attributes of the freshly made Option object. Chief among the option attributes is `action`, which goes a long way toward dictating which other attributes apply or are mandatory. Should you pass irrelevant option attributes, or omit required ones, `optparse` raises an `OptionError` exception describing your mistake.

An option's *action* dictates what `optparse` does upon meeting that option on the command line. The standard option actions baked into `optparse` are:

`"store"`

stash this option's argument (default)

`"store_const"`

store a constant value, pre-set via `Option.const`

`"store_true"`

store `True`

`"store_false"`

store `False`

`"append"`

append this option's argument to a list

`"append_const"`

append a constant value to a list, pre-set via `Option.const`

`"count"`

increment a counter by one

`"callback"`

call a specified function

`"help"`

print a usage message including all options and the documentation for them

(When no action is given, the default is `"store"`. For that action, you may additionally provide `type` and `dest` option attributes; see Standard option actions.)

As is apparent, the bulk of actions come down to storing or updating some value. To that end `optparse` always builds a dedicated object, by convention named `options`, that is an instance of `optparse.Values`.

[Subject index](INDEX.md) · [Previous](populating-the-parser.md) · [Continue](optparse-values-class.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

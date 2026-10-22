# optparse: `optparse.Values`

*class *optparse.Values

An object that keeps parsed argument names and values as its attributes. It is usually produced during a `OptionParser.parse_args()` call, and a custom subclass passed to the *values* argument of `OptionParser.parse_args()` can override it (as described in Parsing arguments).

This object stores option arguments (along with sundry other values) as attributes, keyed by the `dest` (destination) option attribute.

For example, when you call

```python
parser.parse_args()

```

among the very first things `optparse` does is build the `options` object:

```python
options = Values()

```

If one of the options in this parser is defined with

```python
parser.add_option("-f", "--file", action="store", type="string", dest="filename")

```

and the command-line being parsed includes any of the following:

```python
-ffoo
-f foo
--file=foo
--file foo

```

then `optparse`, upon encountering this option, performs the equivalent of

```python
options.filename = "foo"

```

The `type` and `dest` option attributes are nearly as crucial as `action`, but `action` is the sole one that applies to *every* option.

[Subject index](INDEX.md) · [Previous](optionparser-add-option.md) · [Continue](optparse-option-class.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: Defining options](optionparser-add-option.md)

# optparse - Adding new types

### Adding new types

Adding new types means defining your own subclass of `optparse`'s `Option` class. That class carries a couple of attributes defining `optparse`'s types: `TYPES` and `TYPE_CHECKER`.

 Option.TYPES

A tuple of type names; within your subclass, just declare a fresh `TYPES` tuple that extends the standard one.

 Option.TYPE_CHECKER

A dictionary that maps each type name onto a type-checking function. Such a type-checking function carries this signature:

```python
def check_mytype(option, opt, value)

```

in which `option` is an `Option` instance, `opt` is an option string (for instance, `-f`), and `value` is the command-line string that has to be validated and converted into the type you want. `check_mytype()` should give back an object of the hypothetical type `mytype`. Whatever a type-checking function returns ends up either in the OptionValues instance that `OptionParser.parse_args()` returns, or handed to a callback through the `value` parameter.

Your type-checking function ought to raise `OptionValueError` should it hit any trouble. `OptionValueError` accepts a single string argument, which is handed verbatim to `OptionParser`'s `error()` method, which in turn prefixes the program name plus the string `"error:"` and writes the whole thing to stderr before ending the process.

Here's a silly example showing how to add a `"complex"` option type for parsing Python-style complex numbers off the command line. (This is sillier still than it once was, since `optparse` 1.3 added built-in support for complex numbers, but never mind.)

First, the necessary imports:

```python
from copy import copy
from optparse import Option, OptionValueError

```

You have to define your type-checker first, because it gets referenced later (in the `TYPE_CHECKER` class attribute of your Option subclass):

```python
def check_complex(option, opt, value):
    try:
        return complex(value)
    except ValueError:
        raise OptionValueError(
            "option %s: invalid complex value: %r" % (opt, value))

```

Finally, the Option subclass:

```python
class MyOption (Option):
    TYPES = Option.TYPES + ("complex",)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["complex"] = check_complex

```

(Had we skipped making a [`copy()`](https://docs.python.org/3.14/library/copy.html#module-copy) of `Option.TYPE_CHECKER`, we'd have wound up altering the `TYPE_CHECKER` attribute of `optparse`'s Option class. Being Python, nothing prevents you from doing exactly that except good manners and common sense.)

That's all there is to it! Now you can write a script using the new option type just like any other `optparse`-based script, except you must direct your OptionParser to use MyOption rather than Option:

```python
parser = OptionParser(option_class=MyOption)
parser.add_option("-c", type="complex")

```

Or instead, you can assemble your own option list and pass it to OptionParser; when you don't use `add_option()` in the manner above, there's no need to tell OptionParser which option class to use:

```python
option_list = [MyOption("-c", action="store", type="complex", dest="c")]
parser = OptionParser(option_list=option_list)

```

[Subject index](INDEX.md) · [Previous](extending-optparse.md) · [Continue](option-actions-to-option-always-typed-actions.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

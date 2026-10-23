# optparse - Parsing arguments

### Parsing arguments

The entire reason for building and filling an OptionParser is so you can invoke its `parse_args()` method.

 OptionParser.parse_args(*args=None*, *values=None*)

Parse the command-line options found in *args*.

The input parameters are

`args`

the argument list to work through (default: `sys.argv[1:]`)

`values`

a `Values` object in which option arguments will be kept (default: a fresh `Values` instance) – hand over an existing object and the option defaults won't be initialized on it

and what comes back is a pair `(options, args)` in which

`options`

is the very object you passed in as *values*, or else the `optparse.Values` instance that `optparse` built

`args`

is whatever positional arguments remain once every option has been processed

The most frequent usage passes neither keyword argument. When you do pass `values`, it gets mutated through repeated [`setattr()`](https://docs.python.org/3.14/library/functions.html#setattr) calls (roughly one per option argument stored to a destination) and then returned by `parse_args()`.

Whenever `parse_args()` runs into errors within the argument list, it calls the OptionParser's `error()` method with a suitable end-user error message. That ends up terminating your process with an exit status of 2 (the customary Unix exit status for command-line errors).

[Subject index](INDEX.md) · [Previous](standard-option-types.md) · [Continue](option-parser-interspersing-and-option-removal.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

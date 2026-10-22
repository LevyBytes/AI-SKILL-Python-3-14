# string.Formatter: `format()`, `vformat()`, `parse()`, `get_field()`, `get_value()`, `check_unused_args()`, `format_field()`, `convert_field()`

format(*format_string*, */*, **args*, ***kwargs*)

The primary API method. It accepts a format string plus any mix of positional and keyword arguments. The call merely forwards to `vformat()`.

Changed in version 3.7: A format string argument is now [positional-only](https://docs.python.org/3.14/glossary.html#positional-only-parameter).

 vformat(*format_string*, *args*, *kwargs*)

The genuine formatting work happens here. It stands as its own function so that, rather than spreading a dictionary into individual arguments with the `*args` and `**kwargs` syntax and then reassembling it, you can supply a ready-made dictionary of arguments directly. `vformat()` splits the format string apart into character data and replacement fields. The methods listed below are invoked along the way.

On top of those, the `Formatter` supplies several methods meant for subclasses to override:

 parse(*format_string*)

Walk through the format_string and yield an iterable of tuples (*literal_text*, *field_name*, *format_spec*, *conversion*). `vformat()` relies on this to split the string into either literal text or replacement fields.

Each tuple's values represent, in concept, a stretch of literal text paired with one replacement field. When literal text is absent (as happens when two replacement fields sit back-to-back), *literal_text* comes back as a zero-length string. When a replacement field is absent, *field_name*, *format_spec* and *conversion* each hold `None`. The *field_name* value stays as-is, and `vformat()` handles the auto-numbering of positional fields that carry no number.

 get_field(*field_name*, *args*, *kwargs*)

Given *field_name*, turn it into an object ready for formatting. The auto-numbering of any *field_name* coming back from `parse()` happens in `vformat()` ahead of this call. Returns a tuple (obj, used_key). By default it accepts strings shaped as defined in [**PEP 3101**](https://peps.python.org/pep-3101/), such as “0[name]” or “label.title”. The *args* and *kwargs* are whatever was supplied to `vformat()`. That returned *used_key* carries the same sense as the *key* parameter of `get_value()`.

 get_value(*key*, *args*, *kwargs*)

Fetch the value of a particular field. The *key* argument arrives as either an integer or a string. An integer stands for the position of the positional argument inside *args*; a string stands for a named argument inside *kwargs*.

The *args* parameter holds the list of positional arguments handed to `vformat()`, while the *kwargs* parameter holds the dictionary of keyword arguments.

When field names are compound, these functions run only for the field name's first component; the remaining components flow through ordinary attribute and indexing operations.

Thus, for instance, the field expression ‘0.name’ leads to `get_value()` being invoked with a *key* argument of 0. Once `get_value()` returns, the `name` attribute is resolved by a call to the built-in [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) function.

Should the index or keyword point at an item that is missing, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) or [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) ought to be raised.

 check_unused_args(*used_args*, *args*, *kwargs*)

Provide a check for unused arguments where you want one. What this function receives is the full set of argument keys that the format string actually referenced (integers for positional arguments, strings for named ones), together with a reference to the *args* and *kwargs* that reached vformat. From these parameters the collection of unused args can be worked out. `check_unused_args()` is expected to raise an exception when the check does not pass.

 format_field(*value*, *format_spec*)

`format_field()` just defers to the global [`format()`](https://docs.python.org/3.14/library/functions.html#format) built-in. Having it as a method lets subclasses replace it.

 convert_field(*value*, *conversion*)

Converts the value (as returned by `get_field()`) according to a conversion type (matching the one in the tuple that `parse()` produces). Out of the box it recognizes the ‘s’ (str), ‘r’ (repr) and ‘a’ (ascii) conversion types.

[Subject index](INDEX.md) · [Previous](string-formatter-class.md) · [Continue](format-string-syntax.md) · [Owning module, declaration or section: string](string-common-string-operations.md) · [Owning module, declaration or section: string.Formatter](string-formatter-class.md) · [Owning module, declaration or section: Custom string formatting](string-formatter-class.md)

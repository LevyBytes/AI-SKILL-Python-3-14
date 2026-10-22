# string — Format string syntax

### Format string syntax

For format strings, the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method and the `Formatter` class use one common syntax (though with `Formatter`, subclasses may set up a format-string syntax of their own). That syntax resembles the syntax of [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and [template string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings), yet it stays simpler and, notably, accepts no arbitrary expressions inside interpolations.

Within format strings, “replacement fields” are wrapped in curly braces `{}`. Whatever lies outside the braces counts as literal text and is reproduced verbatim in the output. Should you want a brace character inside the literal text, double it to escape it: `{{` and `}}`.

A replacement field follows this grammar:

```text

replacement_field: "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name:        arg_name ("." attribute_name | "[" element_index "]")*
arg_name:          [identifier | digit+]
attribute_name:    identifier
element_index:     digit+ | index_string
index_string:      <any source character except "]"> +
conversion:        "r" | "s" | "a"
format_spec:       format-spec:format_spec
```

Put more plainly, a replacement field may open with a *field_name* identifying the object whose value gets formatted and dropped into the output where the replacement field sits. After the *field_name* you may optionally place a *conversion* field, introduced by an exclamation point `'!'`, and a *format_spec*, introduced by a colon `':'`. Together these set a non-default format for the value being substituted.

See also the Format specification mini-language section.

The *field_name* itself opens with an *arg_name* that is either a number or a keyword. A number points at a positional argument; a keyword points at a named keyword argument. An *arg_name* counts as a number whenever invoking [`str.isdecimal()`](https://docs.python.org/3.14/library/stdtypes.html#str.isdecimal) on the string would yield true. When a format string's numerical arg_names run 0, 1, 2, … in order, you may drop them all (not merely a few), and the numbers 0, 1, 2, … get filled in automatically in that sequence. Since *arg_name* carries no quotes, you cannot name arbitrary dictionary keys (for example, the strings `'10'` or `':-]'`) inside a format string. Any number of index or attribute expressions may trail the *arg_name*. An expression shaped `'.name'` picks out the named attribute via [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr), whereas an expression shaped `'[index]'` performs an index lookup via [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__).

Changed in version 3.1: The positional argument specifiers can be omitted for [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), so `'{} {}'.format(a, b)` is equivalent to `'{0} {1}'.format(a, b)`.

Changed in version 3.4: The positional argument specifiers can be omitted for `Formatter`.

A few straightforward format string examples:

```python
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

```

Before formatting begins, the *conversion* field forces a type coercion. As a rule, formatting a value is the responsibility of that value's own [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) method. Even so, there are moments when you want to compel a type to be rendered as a string, setting aside its own formatting definition. Coercing the value into a string ahead of the `__format__()` call sidesteps the usual formatting logic.

At present three conversion flags exist: `'!s'`, which invokes [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) on the value, `'!r'`, which invokes [`repr()`](https://docs.python.org/3.14/library/functions.html#repr), and `'!a'`, which invokes [`ascii()`](https://docs.python.org/3.14/library/functions.html#ascii).

A few examples:

```python
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first

```

The *format_spec* field holds a description of how the value ought to be displayed, covering particulars like field width, alignment, padding, decimal precision, and the rest. Every value type is free to set its own “formatting mini-language” or reading of the *format_spec*.

A shared formatting mini-language, covered in the section that follows, is supported by most built-in types.

A *format_spec* field may further carry nested replacement fields inside itself. Such nested replacement fields can include a field name, a conversion flag, and a format specification, yet nesting any deeper is disallowed. Those replacement fields inside the format_spec get substituted before the *format_spec* string itself is read. This lets a value's formatting be specified on the fly.

See the Format examples section for some examples.

[Subject index](INDEX.md) · [Previous](string-formatter-format-to-string-formatter-convert-field.md) · [Continue](format-specification-overview.md) · [Owning module, declaration or section: string](string-common-string-operations.md)

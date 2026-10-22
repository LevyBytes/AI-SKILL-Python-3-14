# string: Template source-string attribute

template

This holds the object that was handed to the constructor's *template* argument. As a rule you ought to leave it alone, though read-only access isn't enforced.

Below is an illustration of putting a Template to use:

```python
>>> from string import Template
>>> s = Template('$who likes $what')
>>> s.substitute(who='tim', what='kung pao')
'tim likes kung pao'
>>> d = dict(who='tim')
>>> Template('Give $who $100').substitute(d)
Traceback (most recent call last):
...
ValueError: Invalid placeholder in string: line 1, col 11
>>> Template('$who likes $what').substitute(d)
Traceback (most recent call last):
...
KeyError: 'what'
>>> Template('$who likes $what').safe_substitute(d)
'tim likes $what'

```

For more advanced needs, you may subclass `Template` to tailor the placeholder syntax, the delimiter character, or the whole regular expression that parses template strings. Pulling that off means overriding these class attributes:

- *delimiter* – the literal string that marks the delimiter introducing a placeholder. Its default value is `$`. Keep in mind this should *not* be a regular expression, since the implementation runs [`re.escape()`](https://docs.python.org/3.14/library/re.html#re.escape) over this string whenever needed. Note too that the delimiter can't be altered once the class exists (that is, a different delimiter has to be assigned in the subclass's class namespace).

- *idpattern* – the regular expression laying out the pattern for placeholders without braces. Its default value is the regular expression `(?a:[_a-z][_a-z0-9]*)`. When you supply this and *braceidpattern* is `None`, the same pattern carries over to braced placeholders as well.

Note

Because the default *flags* is `re.IGNORECASE`, the pattern `[a-z]` can wind up matching certain non-ASCII characters. That is the reason the local `a` flag appears here.

Changed in version 3.7: *braceidpattern* can serve to set up separate patterns for use inside versus outside the braces.

- *braceidpattern* – akin to *idpattern*, but it lays out the pattern for braced placeholders. It defaults to `None`, signaling a fall back to *idpattern* (so the one pattern serves both inside and outside braces). Supplied, it lets you set distinct patterns for braced versus unbraced placeholders.

Added in version 3.7.

- *flags* – the regular expression flags brought to bear when compiling the regular expression that recognizes substitutions. Its default value is `re.IGNORECASE`. Be aware that `re.VERBOSE` is always folded into the flags, so any custom *idpattern*s have to obey the conventions of verbose regular expressions.

Added in version 3.2.

As another option, you can hand over the whole regular expression pattern by overriding the class attribute *pattern*. Go that route and the value has to be a regular expression object carrying four named capturing groups. Those capturing groups map onto the rules laid out above, plus the invalid placeholder rule:

- *escaped* – within the default pattern, this group matches the escape sequence, for instance `$$`.

- *named* – this group matches the unbraced placeholder name; the delimiter ought not to be taken into the capturing group.

- *braced* – this group matches the placeholder name wrapped in braces; neither the delimiter nor the braces ought to land in the capturing group.

- *invalid* – this group matches any leftover delimiter pattern (commonly a lone delimiter), and it belongs at the very end of the regular expression.

This class's methods will raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever the pattern matches the template yet none of these named groups matches.

[Subject index](INDEX.md) · [Previous](string-template-substitute-to-string-template-get-identifiers.md) · [Continue](string-capwords.md) · [Owning module, declaration or section: string](string-common-string-operations.md) · [Owning module, declaration or section: string.Template](string-template-class.md) · [Owning module, declaration or section: Template strings ($-strings)](string-template-class.md)

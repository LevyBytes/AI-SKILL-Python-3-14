# configparser.ConfigParser: `getint()`, `getfloat()`, `getboolean()`, `items()`, `set()`, `write()`, `remove_option()`, `remove_section()`, `optionxform()`

getint(*section*, *option*, ***, *raw=False*, *vars=None*[, *fallback*])

A convenience method that coerces the *option* in the named *section* into an integer. Refer to `get()` for what *raw*, *vars* and *fallback* mean.

 getfloat(*section*, *option*, ***, *raw=False*, *vars=None*[, *fallback*])

A convenience method that coerces the *option* in the named *section* into a floating-point number. Refer to `get()` for what *raw*, *vars* and *fallback* mean.

 getboolean(*section*, *option*, ***, *raw=False*, *vars=None*[, *fallback*])

A convenience method that coerces the *option* in the named *section* into a Boolean value. Be aware that the option's accepted values are `'1'`, `'yes'`, `'true'`, and `'on'`, which make this method return `True`, along with `'0'`, `'no'`, `'false'`, and `'off'`, which make it return `False`. Matching against these strings ignores case. Any other value makes it raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Refer to `get()` for what *raw*, *vars* and *fallback* mean.

 items(*raw=False*, *vars=None*)

 items(*section*, *raw=False*, *vars=None*)

With *section* omitted, return a list of *section_name*, *section_proxy* pairs, DEFAULTSECT included.

Otherwise, return a list of *name*, *value* pairs for the options inside the given *section*. The optional arguments carry the same meaning as in the `get()` method.

Changed in version 3.8: Entries found in *vars* are now kept out of the result. Earlier, the output blended genuine parser options together with the variables supplied for interpolation.

 set(*section*, *option*, *value*)

When the given section exists, set the given option to the supplied value; otherwise raise `NoSectionError`. Both *option* and *value* have to be strings; otherwise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

 write(*fileobject*, *space_around_delimiters=True*)

Write a representation of the configuration to the given [file object](https://docs.python.org/3.14/glossary.html#term-file-object), which has to be opened in text mode (so it accepts strings). A later `read()` call can parse this representation back. When *space_around_delimiters* is true, the delimiters separating keys and values are padded with spaces.

Changed in version 3.14: Raises InvalidWriteError whenever the resulting representation could not be read back faithfully by a later `read()` call on this same parser.

Note

When the configuration is written back, comments from the original configuration file are dropped. What counts as a comment depends on the values supplied for *comment_prefix* and *inline_comment_prefix*.

 remove_option(*section*, *option*)

Remove the given *option* from the given *section*. When the section is absent, raise `NoSectionError`. When an option existed and was removed, return [`True`](https://docs.python.org/3.14/library/constants.html#True); otherwise return [`False`](https://docs.python.org/3.14/library/constants.html#False).

 remove_section(*section*)

Remove the given *section* from the configuration. When the section did indeed exist, return `True`. Otherwise return `False`.

 optionxform(*option*)

Convert the option name *option*, whether it arrived from an input file or was handed in by client code, into the form the internal structures will use. By default the implementation returns *option* lowercased; a subclass may replace it, or client code may attach an instance attribute under this name to alter the behavior.

You needn't subclass the parser to take advantage of this method — it can equally be set on an instance to point at any callable accepting one string and yielding a string. Assigning `str`, say, would render option names case sensitive:

```python
cfgparser = ConfigParser()
cfgparser.optionxform = str

```

Bear in mind that when configuration files are read, whitespace around the option names is stripped before `optionxform()` runs.

[Subject index](INDEX.md) · [Previous](config-parser-defaults-sections-and-get.md) · [Continue](unnamed-sections-and-interpolation-limit.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: configparser.ConfigParser](configparser-configparser-class.md) · [Owning module, declaration or section: ConfigParser Objects](configparser-configparser-class.md)

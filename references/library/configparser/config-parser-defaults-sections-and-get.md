# configparser.ConfigParser: `defaults()`, `sections()`, `add_section()`, `has_section()`, `options()`, `has_option()`, `read()`, `read_file()`, `read_string()`, `read_dict()`, `get()`

defaults()

Return a dictionary holding the instance-wide defaults.

 sections()

Return a list of the available sections; the *default section* is left out of the list.

 add_section(*section*)

Add a section named *section* to the instance. When a section of that name is already present, `DuplicateSectionError` is raised. When the *default section* name is supplied, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. The section name has to be a string; otherwise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

Changed in version 3.2: Non-string section names raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 has_section(*section*)

Reports whether the named *section* exists in the configuration. The *default section* is not counted.

 options(*section*)

Return a list of options available in the specified *section*.

 has_option(*section*, *option*)

When the given *section* exists and holds the given *option*, return [`True`](https://docs.python.org/3.14/library/constants.html#True); otherwise return [`False`](https://docs.python.org/3.14/library/constants.html#False). When the specified *section* is [`None`](https://docs.python.org/3.14/library/constants.html#None) or an empty string, DEFAULT is assumed.

 read(*filenames*, *encoding=None*)

Try to read and parse an iterable of filenames, returning the list of filenames that parsed successfully.

When *filenames* is a string, a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object), it is handled as one filename. When a file listed in *filenames* cannot be opened, that file is skipped. The design lets you hand over an iterable of candidate configuration file locations — say, the working directory, a user's home folder, plus a directory shared across the whole system — after which every configuration file present in the iterable gets read.

When none of the listed files exist, the `ConfigParser` instance ends up with an empty dataset. An application that needs starting values loaded from a file should load the mandatory file or files via `read_file()` before it calls `read()` for any optional ones:

```python
import configparser, os

config = configparser.ConfigParser()
config.read_file(open('defaults.cfg'))
config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')],
            encoding='cp1250')

```

Changed in version 3.2: The *encoding* parameter was added. Before that, every file got read with whatever default encoding [`open()`](https://docs.python.org/3.14/library/functions.html#open) used.

Changed in version 3.6.1: The *filenames* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: The *filenames* parameter accepts a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

 read_file(*f*, *source=None*)

Read and parse configuration data out of *f*, which has to be an iterable yielding Unicode strings (for instance files opened in text mode).

The optional *source* argument supplies the name of the file being read. When it's omitted and *f* carries a `name` attribute, that attribute serves as *source*; otherwise the default is `'<???>'`.

Added in version 3.2: Replaces `readfp()`.

 read_string(*string*, *source='&lt;string&gt;'*)

Parse configuration data from a string.

The optional *source* argument supplies a context-specific name for the string passed in. When omitted, `'<string>'` is used. Typically this is a filesystem path or a URL.

Added in version 3.2.

 read_dict(*dictionary*, *source='&lt;dict&gt;'*)

Load configuration out of any object exposing a dict-like `items()` method. Keys serve as section names, and values are dictionaries whose keys and values should appear in the section. When the dictionary type preserves order, sections and their keys are added in order. Values are converted to strings automatically.

The optional *source* argument supplies a context-specific name for the dictionary passed in. When omitted, `<dict>` is used.

You can use this method to copy state from one parser to another.

Added in version 3.2.

 get(*section*, *option*, ***, *raw=False*, *vars=None*[, *fallback*])

Get an *option* value for the named *section*. When *vars* is supplied, it has to be a dictionary. Lookup of *option* proceeds through *vars* (when supplied), *section*, then *DEFAULTSECT*, in that order. When the key isn't found and *fallback* is supplied, that fallback value is used. `None` is acceptable as a *fallback* value.

Unless the *raw* argument is true, every `'%'` interpolation in the returned values is expanded. Interpolation keys are resolved the same way the option itself is.

Changed in version 3.2: The *raw*, *vars* and *fallback* arguments became keyword only, which stops users from mistakenly passing the third positional argument as the *fallback* fallback (a trap especially likely with the mapping protocol).

[Subject index](INDEX.md) · [Previous](configparser-configparser-class.md) · [Continue](config-parser-conversion-and-option-transformation.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: configparser.ConfigParser](configparser-configparser-class.md) · [Owning module, declaration or section: ConfigParser Objects](configparser-configparser-class.md)

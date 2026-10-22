# logging.config — Dictionary Schema Details — Section introduction and initial examples

### Dictionary Schema Details

These keys must appear in the dictionary handed to `dictConfig()`:

- *version* - which should be set to an integer representing the schema version. At the moment the sole valid value is 1, but holding this key lets the schema grow over time while still keeping backwards compatibility.

Every other key is optional, though when present it is read as described below. Throughout the cases below where a 'configuring dict' is referenced, it is inspected for the special `'()'` key to determine whether custom instantiation is called for. When it is, the mechanism laid out in User-defined objects below builds an instance; if not, the context decides what to instantiate.

- *formatters* - the matching value is a dict where each key is a formatter id and each value is a dict spelling out how to configure the matching [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) instance.

The configuring dict is scanned for these optional keys, which line up with the arguments handed in to build a [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) object:

  - `format`

  - `datefmt`

  - `style`

  - `validate` (since version >=3.8)

  - `defaults` (since version >=3.12)

An optional `class` key names the formatter's class (given as a dotted module-and-class name). The instantiation arguments match those for [`Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter), so this key is chiefly handy for building a customised subclass of `Formatter`. For instance, the alternate class could lay out exception tracebacks in an expanded or condensed style. Should your formatter call for different or additional configuration keys, you should turn to User-defined objects.

- *filters* - the matching value is a dict where each key is a filter id and each value is a dict spelling out how to configure the matching Filter instance.

The configuring dict is scanned for the key `name` (which defaults to the empty string), and this is used to build a [`logging.Filter`](https://docs.python.org/3.14/library/logging.html#logging.Filter) instance.

- *handlers* - the matching value is a dict where each key is a handler id and each value is a dict spelling out how to configure the matching Handler instance.

The configuring dict is scanned for these keys:

  - `class` (mandatory). This is the fully qualified name of the handler class.

  - `level` (optional). The level of the handler.

  - `formatter` (optional). The id of the formatter for this handler.

  - `filters` (optional). A list of ids of the filters for this handler.

Changed in version 3.11: besides ids, `filters` now accepts filter instances as well.

Every *other* key is forwarded as a keyword argument to the handler's constructor. For example, given the snippet:

[Subject index](INDEX.md) · [Previous](configuration-dictionary-schema.md) · [Continue](dictionary-schema-details-code-example-handlers.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)

# logging.config - User-defined objects

### User-defined objects

The schema accommodates user-defined objects for handlers, filters and formatters. (Loggers have no need for distinct types across distinct instances, so this configuration schema offers no support for user-defined logger classes.)

Objects awaiting configuration are spelled out by dictionaries that detail how they are configured. In certain spots the logging system can deduce from the context how an object should be built, but when a user-defined object needs building, the system has no way to know how. To deliver full flexibility for building user-defined objects, the user must supply a 'factory' — a callable that is invoked with a configuration dictionary and that returns the built object. This is flagged by an absolute import path to the factory being placed under the special key `'()'`. Here's a concrete example:

```yaml
formatters:
  brief:
    format: '%(message)s'
  default:
    format: '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
    datefmt: '%Y-%m-%d %H:%M:%S'
  custom:
      (): my.package.customFormatterFactory
      bar: baz
      spam: 99.9
      answer: 42

```

The YAML snippet above sets out three formatters. The first, with id `brief`, is an ordinary [`logging.Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) instance carrying the given format string. The second, with id `default`, carries a lengthier format and additionally states the time format outright, and will yield a `logging.Formatter` set up with those two format strings. Rendered in Python source form, the `brief` and `default` formatters have these configuration sub-dictionaries:

```python
{
  'format' : '%(message)s'
}

```

and:

```python
{
  'format' : '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
  'datefmt' : '%Y-%m-%d %H:%M:%S'
}

```

respectively, and because these dictionaries hold no special key `'()'`, the building is deduced from the context: consequently, ordinary [`logging.Formatter`](https://docs.python.org/3.14/library/logging.html#logging.Formatter) instances result. The configuration sub-dictionary for the third formatter, with id `custom`, is:

```python
{
  '()' : 'my.package.customFormatterFactory',
  'bar' : 'baz',
  'spam' : 99.9,
  'answer' : 42
}

```

and this one carries the special key `'()'`, signalling that user-defined building is desired. Here, the named factory callable will be employed. If it is an actual callable it gets used directly — otherwise, when you give a string (as in the example) the actual callable gets located through the normal import mechanisms. The callable gets invoked with the **remaining** items from the configuration sub-dictionary as keyword arguments. In the example above, the formatter with id `custom` will be taken to be the return value of the call:

```python
my.package.customFormatterFactory(bar='baz', spam=99.9, answer=42)

```

Warning

The values for keys like `bar`, `spam` and `answer` in the example above ought not to be configuration dictionaries or references such as `cfg://foo` or `ext://bar`, because the configuration machinery won't process them but will instead hand them to the callable as-is.

The key `'()'` was chosen as the special key because it isn't a valid keyword parameter name, so it won't collide with the names of the keyword arguments used in the call. The `'()'` doubles as a mnemonic that the matching value is a callable.

Changed in version 3.11: On both `handlers` and `loggers`, the `filters` member now accepts filter instances as well as ids.

You can additionally state a special key `'.'` that maps attribute names onto their values. When found, the named attributes will be set on the user-defined object before it is handed back. Thus, with the configuration that follows:

```python
{
  '()' : 'my.package.customFormatterFactory',
  'bar' : 'baz',
  'spam' : 99.9,
  'answer' : 42,
  '.' : {
    'foo': 'bar',
    'baz': 'bozz'
  }
}
```

the formatter that comes back will have attribute `foo` set to `'bar'` and attribute `baz` set to `'bozz'`.

Warning

The values for attributes like `foo` and `baz` in the example above ought not to be configuration dictionaries or references such as `cfg://foo` or `ext://bar`, because the configuration machinery won't process them but will instead set them as attribute values as-is.

[Subject index](INDEX.md) · [Previous](object-connections.md) · [Continue](access-to-external-objects.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)

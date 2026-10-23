# configparser - Legacy API Examples - Section introduction and initial examples

### Legacy API Examples

Largely for backwards compatibility reasons, `configparser` also ships a legacy API with explicit `get`/`set` methods. The approaches described below do have legitimate uses, yet new projects are encouraged to prefer mapping protocol access. The legacy API can be more advanced, lower-level, and at points genuinely counterintuitive.

An example of writing to a configuration file:

```python
import configparser

config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'w') as configfile:
    config.write(configfile)

```

An example of reading the configuration file again:

```python
import configparser

config = configparser.RawConfigParser()
config.read('example.cfg')

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types
a_float = config.getfloat('Section1', 'a_float')
an_int = config.getint('Section1', 'an_int')
print(a_float + an_int)

# Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
# This is because we are using a RawConfigParser().
if config.getboolean('Section1', 'a_bool'):
    print(config.get('Section1', 'foo'))

```

To get interpolation, use `ConfigParser`:

[Subject index](INDEX.md) · [Previous](configparser-optionxform-to-configparser-sectcre.md) · [Continue](legacy-api-examples-code-example-import-configparser.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)

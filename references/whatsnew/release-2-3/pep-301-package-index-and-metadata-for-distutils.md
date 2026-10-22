# What’s New in Python 2.3 / PEP 301: Package Index and Metadata for Distutils

### PEP 301: Package Index and Metadata for Distutils

The Python catalog people had been asking after for ages shows up for the first time in 2.3.

At the core of the catalog sits the new Distutils **register** command. Invoke `python setup.py register` to gather a package's metadata — name, version, maintainer, description, and so on — and ship it off to a central catalog server. You can browse the catalog that results at [https://pypi.org](https://pypi.org).

The Distutils `setup()` function picked up a new optional *classifiers* keyword argument to give the catalog extra value. You can pass a list of [Trove](http://catb.org/~esr/trove/)-style strings to help categorize the software.

Below is a sample `setup.py` carrying classifiers, written so it still works with older Distutils releases:

```python
from distutils import core
kw = {'name': "Quixote",
      'version': "0.5.1",
      'description': "A highly Pythonic Web application framework",
      # ...
      }

if (hasattr(core, 'setup_keywords') and
    'classifiers' in core.setup_keywords):
    kw['classifiers'] = \
        ['Topic :: Internet :: WWW/HTTP :: Dynamic Content',
         'Environment :: No Input/Output (Daemon)',
         'Intended Audience :: Developers'],

core.setup(**kw)

```

To see every classifier, run `python setup.py register --list-classifiers`.

See also

[**PEP 301**](https://peps.python.org/pep-0301/) - Package Index and Metadata for Distutils

Written and implemented by Richard Jones.

[Subject index](INDEX.md) · [Previous source section](pep-293-codec-error-handling-callbacks.md) · [Next source section](pep-302-new-import-hooks.md) · [Release/subject declaration](standard-set-type.md)

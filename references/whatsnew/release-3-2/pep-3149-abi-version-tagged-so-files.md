# What's New In Python 3.2 / PEP 3149: ABI Version Tagged .so Files — sysconfig

### PEP 3149: ABI Version Tagged .so Files

Whereas the PYC repository directory lets several bytecode caches sit side by side, this PEP brings a comparable scheme to shared object files, granting them one shared directory plus a distinct name per version.

That shared directory is "pyshared", and the names are kept distinct by encoding the Python implementation (CPython, PyPy, Jython, and the like), the major plus minor version numbers, and any build flags (for instance "d" for debug, "m" for pymalloc, "u" for wide-unicode). For some package "foo", installing the distribution package might leave you with these files:

```python
/usr/share/pyshared/foo.cpython-32m.so
/usr/share/pyshared/foo.cpython-33md.so

```

From within Python, these tags are obtainable through functions in the [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) module:

```python
>>> import sysconfig
>>> sysconfig.get_config_var('SOABI')       # find the version tag
'cpython-32mu'
>>> sysconfig.get_config_var('EXT_SUFFIX')  # find the full filename extension
'.cpython-32mu.so'

```

See also

[**PEP 3149**](https://peps.python.org/pep-3149/) - ABI Version Tagged .so Files

PEP written by Barry Warsaw.

[Subject index](INDEX.md) · [Previous source section](pep-3147-pyc-repository-directories.md) · [Next source section](pep-3333-python-web-server-gateway-interface-v1-0-1.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

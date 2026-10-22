# sysconfig — Configuration variables

### Configuration variables

Bundled with a Python distribution are a `Makefile` and a `pyconfig.h` header file, both required for compiling the Python binary itself as well as third-party C extensions built through `setuptools`.

Every variable drawn from these files is gathered by `sysconfig` into a dictionary you can reach via `get_config_vars()` or `get_config_var()`.

Bear in mind that the set is considerably smaller on Windows.

 sysconfig.get_config_vars(**args*)

Called without arguments, it yields a dictionary holding every configuration variable that applies to the platform you are on.

Called with arguments, it yields a list of the values produced by looking each argument up in the configuration-variable dictionary.

Whenever an argument's value cannot be found, `None` is returned for it.

 sysconfig.get_config_var(*name*)

Yields the value of one variable *name*. The same as `get_config_vars().get(name)`.

Should *name* be absent, `None` comes back.

A usage sample:

```python
>>> import sysconfig
>>> sysconfig.get_config_var('Py_ENABLE_SHARED')
0
>>> sysconfig.get_config_var('LIBDIR')
'/usr/local/lib'
>>> sysconfig.get_config_vars('AR', 'CXX')
['ar', 'g++']

```

[Subject index](INDEX.md) · [Previous](python-configuration-access-overview.md) · [Continue](installation-paths.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)

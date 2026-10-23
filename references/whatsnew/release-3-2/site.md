# What's New In Python 3.2 / site - site

### site

Three additional helpers have arrived in the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module that are handy when you want to report on how a particular Python install is configured.

- [`getsitepackages()`](https://docs.python.org/3.14/library/site.html#site.getsitepackages) enumerates every one of the global site-packages directories.

- [`getuserbase()`](https://docs.python.org/3.14/library/site.html#site.getuserbase) describes the per-user base directory under which data may be kept.

- [`getusersitepackages()`](https://docs.python.org/3.14/library/site.html#site.getusersitepackages) exposes the path to the user-specific site-packages folder.

```python
>>> import site
>>> site.getsitepackages()
['/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/site-packages',
 '/Library/Frameworks/Python.framework/Versions/3.2/lib/site-python',
 '/Library/Python/3.2/site-packages']
>>> site.getuserbase()
'/Users/raymondhettinger/Library/Python/3.2'
>>> site.getusersitepackages()
'/Users/raymondhettinger/Library/Python/3.2/lib/python/site-packages'

```

For convenience, part of what site offers can be reached straight away through the command line:

```shell
$ python -m site --user-base
/Users/raymondhettinger/.local
$ python -m site --user-site
/Users/raymondhettinger/.local/lib/python3.2/site-packages

```

(Contributed by Tarek Ziadé in [bpo-6693](https://bugs.python.org/issue?@action=redirect&bpo=6693).)

[Subject index](INDEX.md) · [Previous source section](ctypes.md) · [Next source section](sysconfig.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

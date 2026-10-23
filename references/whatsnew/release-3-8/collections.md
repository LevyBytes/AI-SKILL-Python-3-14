# What’s New In Python 3.8 / collections - collections

> (Contributed by Matthias Bussonnier in [bpo-34616](https://bugs.python.org/issue?@action=redirect&bpo=34616))

### collections

For [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple), the [`_asdict()`](https://docs.python.org/3.14/library/collections.html#collections.somenamedtuple._asdict) method now yields a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) in place of a [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict). Plain dicts have promised their ordering ever since Python 3.7, so this holds. Should you still want the added capabilities of `OrderedDict`, the recommended fix is converting the output to whatever type you need: `OrderedDict(nt._asdict())`.

[Subject index](INDEX.md) · [Previous source section](builtins.md) · [Next source section](cprofile.md) · [Release/subject declaration](assignment-expressions.md)

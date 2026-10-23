# What’s New In Python 3.8 / Other Language Changes - datetime, decimal, fractions, re, statistics, types

### Other Language Changes

- Owing to an implementation snag, a [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement used to be forbidden inside the [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause. Python 3.8 removes that ban. (Serhiy Storchaka contributed this in [bpo-32489](https://bugs.python.org/issue?@action=redirect&bpo=32489).)

- The [`bool`](https://docs.python.org/3.14/library/functions.html#bool), [`int`](https://docs.python.org/3.14/library/functions.html#int), and [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) types each gained an [`as_integer_ratio()`](https://docs.python.org/3.14/library/stdtypes.html#int.as_integer_ratio) method, mirroring the one already present on [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal). Thanks to this small API extension, you can write `numerator, denominator = x.as_integer_ratio()` and rely on it functioning uniformly across several numeric types. (Lisa Roach contributed this in [bpo-33073](https://bugs.python.org/issue?@action=redirect&bpo=33073), with Raymond Hettinger in [bpo-37819](https://bugs.python.org/issue?@action=redirect&bpo=37819).)

- The constructors for [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`complex`](https://docs.python.org/3.14/library/functions.html#complex) will now fall back on the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) special method whenever it exists and the matching [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__), [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) or [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) method is missing. (Serhiy Storchaka contributed this in [bpo-20092](https://bugs.python.org/issue?@action=redirect&bpo=20092).)

- Support for `\N{*name*}` escapes arrived inside [`regular expressions`](https://docs.python.org/3.14/library/re.html#module-re):

```python
>>> notice = 'Copyright © 2019'
>>> copyright_year_pattern = re.compile(r'\N{copyright sign}\s*(\d{4})')
>>> int(copyright_year_pattern.search(notice).group(1))
2019

```

(Jonathan Eunice and Serhiy Storchaka contributed this in [bpo-30688](https://bugs.python.org/issue?@action=redirect&bpo=30688).)

- Dicts together with their views can now be walked in reversed insertion order by way of [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed). (Rémi Lapeyre contributed this in [bpo-33462](https://bugs.python.org/issue?@action=redirect&bpo=33462).)

- The grammar accepted for keyword names inside function calls grew stricter. Specifically, `f((keyword)=arg)` is no longer permitted. Nothing more than a plain name was ever supposed to be allowed on the left side of a keyword-argument assignment term. (Benjamin Peterson contributed this in [bpo-34641](https://bugs.python.org/issue?@action=redirect&bpo=34641).)

- When you generalize iterable unpacking inside [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) and [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statements, the surrounding parentheses are no longer mandatory. That lines the *yield* and *return* syntax up more closely with ordinary assignment syntax:

```python
>>> def parse(family):
...     lastname, *members = family.split()
...     return lastname.upper(), *members
...
>>> parse('simpsons homer marge bart lisa maggie')
('SIMPSONS', 'homer', 'marge', 'bart', 'lisa', 'maggie')

```

(David Cuthbert and Jordan Chapman contributed this in [bpo-32117](https://bugs.python.org/issue?@action=redirect&bpo=32117).)

- Leave out a comma in something like `[(10, 20) (30, 40)]` and the compiler now raises a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) carrying a useful hint. That beats the old behavior of merely getting a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) telling you the first tuple was not callable. (Serhiy Storchaka contributed this in [bpo-15248](https://bugs.python.org/issue?@action=redirect&bpo=15248).)

- Arithmetic carried out between subclasses of [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) or [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) and [`datetime.timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) objects now yields an instance of the subclass instead of the base class. The same goes for the return type of any operation whose implementation leans, directly or not, on `datetime.timedelta` arithmetic, [`astimezone()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.astimezone) among them. (Paul Ganssle contributed this in [bpo-32417](https://bugs.python.org/issue?@action=redirect&bpo=32417).)

- Should the Python interpreter be interrupted by Ctrl-C (SIGINT) while the resulting [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception goes uncaught, the Python process now leaves by way of a SIGINT signal or with the right exit code, so the parent process can tell that a Ctrl-C killed it. Shells on POSIX and Windows rely on this to cleanly stop scripts during interactive sessions. (Google, through Gregory P. Smith, contributed this in [bpo-1054041](https://bugs.python.org/issue?@action=redirect&bpo=1054041).)

- Certain advanced coding styles call for mutating the [`types.CodeType`](https://docs.python.org/3.14/library/types.html#types.CodeType) object behind an existing function. Code objects being immutable, you have to forge a brand-new one modeled after the existing object — and with 19 parameters, that grew rather tiresome. The new `replace()` method now lets you clone a code object while tweaking just a handful of its parameters.

Here is a sample that rewrites the [`statistics.mean()`](https://docs.python.org/3.14/library/statistics.html#statistics.mean) function so its *data* parameter can no longer be passed as a keyword argument:

```python
>>> from statistics import mean
>>> mean(data=[10, 20, 90])
40
>>> mean.__code__ = mean.__code__.replace(co_posonlyargcount=1)
>>> mean(data=[10, 20, 90])
Traceback (most recent call last):
  ...
TypeError: mean() got some positional-only arguments passed as keyword arguments: 'data'

```

(Victor Stinner contributed this in [bpo-37032](https://bugs.python.org/issue?@action=redirect&bpo=37032).)

[Subject index](INDEX.md) · [Previous source section](pickle-protocol-5-with-out-of-band-data-buffers.md) · [Next source section](modular-inverses-and-language-changes.md) · [Release/subject declaration](assignment-expressions.md)

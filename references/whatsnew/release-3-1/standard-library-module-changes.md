# What’s New In Python 3.1 / New, Improved, and Deprecated Modules - bz2, collections, decimal, fractions, gzip, itertools, tkinter.ttk

### New, Improved, and Deprecated Modules

- A [`collections.Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter) class was added to make tallying the distinct items in a sequence or iterable handy:

```python
>>> Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
Counter({'blue': 3, 'red': 2, 'green': 1})

```

(Contributed by Raymond Hettinger; [bpo-1696199](https://bugs.python.org/issue?@action=redirect&bpo=1696199).)

- A fresh module, [`tkinter.ttk`](https://docs.python.org/3.14/library/tkinter.ttk.html#module-tkinter.ttk), was added to reach the Tk themed widget set. At heart, ttk aims to pull apart, as much as feasible, the code that drives a widget’s behavior from the code that gives it its look.

(Contributed by Guilherme Polo; [bpo-2983](https://bugs.python.org/issue?@action=redirect&bpo=2983).)

- The context management protocol is now honored by the [`gzip.GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) and [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) classes:

```python
>>> # Automatically close file after writing
>>> with gzip.GzipFile(filename, "wb") as f:
...     f.write(b"xxx")

```

(Contributed by Antoine Pitrou.)

- The [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module now offers methods to build a decimal object out of a binary [`float`](https://docs.python.org/3.14/library/functions.html#float). That conversion is precise, though it may occasionally catch you off guard:

```python
>>> Decimal.from_float(1.1)
Decimal('1.100000000000000088817841970012523233890533447265625')

```

That lengthy decimal output reveals the true binary fraction kept for *1.1*. So many digits appear because *1.1* has no exact binary form.

(Contributed by Raymond Hettinger and Mark Dickinson.)

- Two fresh functions arrived in the [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module. Among four tools for producing combinatorics, including permutations and Cartesian products, sits the [`itertools.combinations_with_replacement()`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations_with_replacement) function. The [`itertools.compress()`](https://docs.python.org/3.14/library/itertools.html#itertools.compress) function takes after the one of the same name in APL. Beyond that, the existing [`itertools.count()`](https://docs.python.org/3.14/library/itertools.html#itertools.count) function picks up an optional *step* argument and will work with any kind of counting sequence, [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) included:

```python
>>> [p+q for p,q in combinations_with_replacement('LOVE', 2)]
['LL', 'LO', 'LV', 'LE', 'OO', 'OV', 'OE', 'VV', 'VE', 'EE']

>>> list(compress(data=range(10), selectors=[0,0,1,1,0,1,0,1,0,0]))
[2, 3, 5, 7]

>>> c = count(start=Fraction(1,2), step=Fraction(1,6))
>>> [next(c), next(c), next(c), next(c)]
[Fraction(1, 2), Fraction(2, 3), Fraction(5, 6), Fraction(1, 1)]

```

(Contributed by Raymond Hettinger.)

- [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) now accepts a *rename* keyword argument, which turns invalid fieldnames automatically into positional names shaped like _0, _1, and so on. That helps whenever the field names come from somewhere outside, like a CSV header, a SQL field list, or input from a user:

```python
>>> query = input()
SELECT region, dept, count(*) FROM main GROUPBY region, dept

>>> cursor.execute(query)
>>> query_fields = [desc[0] for desc in cursor.description]
>>> UserQuery = namedtuple('UserQuery', query_fields, rename=True)
>>> pprint.pprint([UserQuery(*row) for row in cursor])
[UserQuery(region='South', dept='Shipping', _2=185),
 UserQuery(region='North', dept='Accounting', _2=37),
 UserQuery(region='West', dept='Sales', _2=419)]

```

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Next source section](io-logging-debugging-and-testing-module-changes.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md)

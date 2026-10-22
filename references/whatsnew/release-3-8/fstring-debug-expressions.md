# What’s New In Python 3.8 / f-strings support `=` for self-documenting expressions and debugging

### f-strings support `=` for self-documenting expressions and debugging

An `=` specifier joined the [f-string](https://docs.python.org/3.14/glossary.html#term-f-string) toolkit. Writing an f-string like `f'{expr=}'` produces the literal text of that expression, followed by an equals sign, followed by the repr of whatever the expression evaluated to. For instance:

```python
>>> import datetime as dt
>>> user = 'eric_idle'
>>> member_since = dt.date(1975, 7, 31)
>>> f'{user=} {member_since=}'
"user='eric_idle' member_since=datetime.date(1975, 7, 31)"

```

You can lean on the ordinary [f-string format specifiers](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) to dictate exactly how the expression’s result is rendered:

```python
>>> delta = dt.date.today() - member_since
>>> f'{user=!s}  {delta.days=:,d}'
'user=eric_idle  delta.days=16,075'

```

Because the `=` specifier echoes back the entire expression, it is handy for surfacing the math behind a result:

```python
>>> print(f'{theta=}  {cos(radians(theta))=:.3f}')
theta=30  cos(radians(theta))=0.866

```

(Eric V. Smith and Larry Hastings contributed this in [bpo-36817](https://bugs.python.org/issue?@action=redirect&bpo=36817).)

[Subject index](INDEX.md) · [Previous source section](debug-build-uses-the-same-abi-as-release-build.md) · [Next source section](pep-578-python-runtime-audit-hooks.md) · [Release/subject declaration](assignment-expressions.md)

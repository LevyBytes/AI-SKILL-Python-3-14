# What’s New in Python 2.4 / PEP 292: Simpler String Substitutions — string

### PEP 292: Simpler String Substitutions

A handful of fresh classes in the standard library supply a different approach for dropping variables into strings; this substitution style can suit applications where users without training have to modify templates.

Substituting variables by name is normally handled through the `%` operator:

```python
>>> '%(page)i: %(title)s' % {'page':2, 'title': 'The Best of Times'}
'2: The Best of Times'

```

While composing the template string, the `i` or `s` trailing the closing parenthesis is easy to leave out. That barely matters when the template lives inside a Python module, since you run the code, get an “Unsupported format character” [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), and patch it. Picture instead an application like Mailman, where the people editing template strings or translations have no familiarity with the Python language. Explaining the format string’s syntax to those users gets complicated, and once they slip up, handing them useful feedback proves hard.

To the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module, PEP 292 contributes a `Template` class that leans on `$` to mark a substitution:

```python
>>> import string
>>> t = string.Template('$page: $title')
>>> t.substitute({'page':2, 'title': 'The Best of Times'})
'2: The Best of Times'

```

Should a key be absent from the dictionary, the `substitute()` method throws a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError). There’s a `safe_substitute()` method as well, which passes over keys that are missing:

```python
>>> t = string.Template('$page: $title')
>>> t.safe_substitute({'page':3})
'3: $title'

```

See also

[**PEP 292**](https://peps.python.org/pep-0292/) - Simpler String Substitutions

Authored and built by Barry Warsaw.

[Subject index](INDEX.md) · [Previous source section](pep-289-generator-expressions.md) · [Next source section](function-method-decorators.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)

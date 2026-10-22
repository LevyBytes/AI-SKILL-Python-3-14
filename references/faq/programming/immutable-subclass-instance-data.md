# How can a subclass control what data is stored in an immutable instance?

### How can a subclass control what data is stored in an immutable instance?

To subclass an immutable type, supply your own [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method rather than [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__). That second method runs only *after* the instance already exists, by which point it is too late to change data inside an immutable instance.

Each of these immutable classes carries a signature that differs from its parent class:

```python
import datetime as dt

class FirstOfMonthDate(dt.date):
    "Always choose the first day of the month"
    def __new__(cls, year, month, day):
        return super().__new__(cls, year, month, 1)

class NamedInt(int):
    "Allow text names for some numbers"
    xlat = {'zero': 0, 'one': 1, 'ten': 10}
    def __new__(cls, value):
        value = cls.xlat.get(value, value)
        return super().__new__(cls, value)

class TitleStr(str):
    "Convert str to name suitable for a URL path"
    def __new__(cls, s):
        s = s.lower().replace(' ', '-')
        s = ''.join([c for c in s if c.isalnum() or c == '-'])
        return super().__new__(cls, s)

```

You can put the classes to use as follows:

```pycon
>>> FirstOfMonthDate(2012, 2, 14)
FirstOfMonthDate(2012, 2, 1)
>>> NamedInt('ten')
10
>>> NamedInt(20)
20
>>> TitleStr('Blog: Why Python Rocks')
'blog-why-python-rocks'

```

[Subject index](INDEX.md)

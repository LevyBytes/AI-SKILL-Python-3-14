# Custom validators

### Custom validators

Below are three handy data-validation helpers:

1.

`OneOf` confirms that a value belongs to a fixed collection of permitted choices.

2.

`Number` confirms that a value is an [`int`](https://docs.python.org/3.14/library/functions.html#int) or a [`float`](https://docs.python.org/3.14/library/functions.html#float). It can optionally confirm that the value falls within a supplied minimum or maximum.

3.

`String` confirms that a value is a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). It can optionally check a supplied minimum or maximum length, and it can also test a caller-supplied [predicate](https://en.wikipedia.org/wiki/Predicate_(mathematical_logic)).

```python
class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(
                f'Expected {value!r} to be one of {self.options!r}'
            )

class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )

class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be a str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be true for {value!r}'
            )

```

[Subject index](INDEX.md) · [Previous source context](validator-class.md) · [Following source context](practical-application.md)

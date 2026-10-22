# How do I write a function with output parameters (call by reference)?

### How do I write a function with output parameters (call by reference)?

Keep in mind that arguments in Python are passed by assignment. Because assignment merely creates references to objects, there's no alias linking an argument name in the caller and the callee, and therefore no call-by-reference. You can produce the effect you're after in several ways.

1.

By returning a tuple of the results:

```python
>>> def func1(a, b):
...     a = 'new-value'        # a and b are local names
...     b = b + 1              # assigned to new objects
...     return a, b            # return new values
...
>>> x, y = 'old-value', 99
>>> func1(x, y)
('new-value', 100)

```

This is almost always the clearest solution.

2.

Through global variables. Doing so lacks thread safety, so it isn’t advised.

3.

By passing a mutable (changeable in-place) object:

```python
>>> def func2(a):
...     a[0] = 'new-value'     # 'a' references a mutable list
...     a[1] = a[1] + 1        # changes a shared object
...
>>> args = ['old-value', 99]
>>> func2(args)
>>> args
['new-value', 100]

```

4.

By passing in a dictionary that gets mutated:

```python
>>> def func3(args):
...     args['a'] = 'new-value'     # args is a mutable dictionary
...     args['b'] = args['b'] + 1   # change it in-place
...
>>> args = {'a': 'old-value', 'b': 99}
>>> func3(args)
>>> args
{'a': 'new-value', 'b': 100}

```

5.

Or bundle up values in a class instance:

```python
>>> class Namespace:
...     def __init__(self, /, **args):
...         for key, value in args.items():
...             setattr(self, key, value)
...
>>> def func4(args):
...     args.a = 'new-value'        # args is a mutable Namespace
...     args.b = args.b + 1         # change object in-place
...
>>> args = Namespace(a='old-value', b=99)
>>> func4(args)
>>> vars(args)
{'a': 'new-value', 'b': 100}

```

There’s almost never a good reason to get this complicated.

Returning a tuple holding the several results is your best bet.

[Subject index](INDEX.md)

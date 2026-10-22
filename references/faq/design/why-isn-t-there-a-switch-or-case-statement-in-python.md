# Why isn't there a switch or case statement in Python?

### Why isn't there a switch or case statement in Python?

Broadly speaking, structured switch statements run one block of code whenever an expression takes on a given value or set of values. From Python 3.10 on, you can readily match literal values, or constants within a namespace, by means of a `match ... case` statement. A longstanding alternative is a chain of `if... elif... elif... else`.

When you must select among a very large set of possibilities, you can build a dictionary that maps case values to functions you'll call. As an example:

```python
functions = {'a': function_1,
             'b': function_2,
             'c': self.method_1}

func = functions[value]
func()

```

For invoking methods on objects, you can streamline things even more by using the [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) built-in to fetch methods by a particular name:

```python
class MyVisitor:
    def visit_a(self):
        ...

    def dispatch(self, value):
        method_name = 'visit_' + str(value)
        method = getattr(self, method_name)
        method()

```

The recommendation is to attach a prefix to the method names, such as `visit_` in this example. Lacking such a prefix, if the values originate from an untrusted source, an attacker could invoke any method whatsoever on your object.

Mimicking switch with fallthrough, in the manner of C's switch-case-default, can be done, but it's considerably harder and less often needed.

[Subject index](INDEX.md)

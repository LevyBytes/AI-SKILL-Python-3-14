# How do I use strings to call functions/methods?

### How do I use strings to call functions/methods?

Several methods exist.

- The best one relies on a dictionary that maps strings onto functions. Its chief benefit is that the strings need not line up with the names of the functions. It is likewise the main technique for emulating a case construct:

```python
def a():
    pass

def b():
    pass

dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs

dispatch[get_input()]()  # Note trailing parens to call function

```

- Reach for the built-in function [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr):

```python
import foo
getattr(foo, 'bar')()

```

Keep in mind that [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) operates on any object at all, classes, class instances, modules, and the rest.

The standard library applies this in a number of spots, such as:

```python
class Foo:
    def do_foo(self):
        ...

    def do_bar(self):
        ...

f = getattr(foo_instance, 'do_' + opname)
f()

```

- Use [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) to look up the function name:

```python
def myFunc():
    print("hello")

fname = "myFunc"

f = locals()[fname]
f()

```

[Subject index](INDEX.md)

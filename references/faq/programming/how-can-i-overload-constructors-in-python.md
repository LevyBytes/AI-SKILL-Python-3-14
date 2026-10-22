# How can I overload constructors (or methods) in Python?

### How can I overload constructors (or methods) in Python?

What follows really covers every method, though this question tends to first arise around constructors.

In C++ you’d write:

```c
class C {
    C() { cout << "No arguments\n"; }
    C(int i) { cout << "Argument is " << i << "\n"; }
}

```

With Python you instead write one constructor that, by means of default arguments, handles all the cases. For example:

```python
class C:
    def __init__(self, i=None):
        if i is None:
            print("No arguments")
        else:
            print("Argument is", i)

```

It’s not a perfect match, but it is near enough for everyday use.

A variable-length argument list is another option you might use, for example:

```python
def __init__(self, *args):
    ...

```

That same pattern applies across all method definitions.

[Subject index](INDEX.md)

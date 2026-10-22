# How can my code discover the name of an object?

### How can my code discover the name of an object?

By and large, it can't, since objects don't truly carry names. Fundamentally, assignment always ties a name to a value; the same goes for `def` and `class` statements, except there the value is a callable. Look at the code below:

```python
>>> class A:
...     pass
...
>>> B = A
>>> a = B()
>>> b = a
>>> print(b)
<__main__.A object at 0x16D07CC>
>>> print(a)
<__main__.A object at 0x16D07CC>

```

You could argue the class does have a name: although it's bound to two names and invoked via the name `B`, the instance that gets created is still reported as an instance of class `A`. Even so, there's no way to tell whether the instance's name is `a` or `b`, because both names are bound to the same value.

As a rule, your code shouldn't have to "know the names" assigned to specific values. Outside of cases where you are intentionally building introspective programs, needing this usually signals that a different approach would serve you better.

On comp.lang.python, Fredrik Lundh once offered a fitting analogy in response to this very question:

>

It works just like learning the name of that stray cat that turned up on your porch: the cat (object) itself won’t tell you its name, nor does it much care – which leaves only one route to discovering what it’s called, namely asking every one of your neighbours (namespaces) whether the cat (object) belongs to them…

…and you shouldn’t be taken aback to discover that it answers to several names, or to none whatsoever!

[Subject index](INDEX.md)

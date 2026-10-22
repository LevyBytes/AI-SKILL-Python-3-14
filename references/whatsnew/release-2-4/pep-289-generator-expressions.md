# What’s New in Python 2.4 / PEP 289: Generator Expressions — itertools

### PEP 289: Generator Expressions

Thanks to the iterator capability that arrived in Python 2.2 plus the [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module, writing programs that iterate across sizable data collections becomes simpler without keeping the whole collection resident in memory at once. List comprehensions sit awkwardly here, since they yield a Python list holding every item. That inevitably drags all the objects into memory, which can become troublesome once your data collection grows quite large. While composing a program in a functional style, the natural impulse would be to write something along these lines:

```python
links = [link for link in get_all_links() if not link.followed]
for link in links:
    ...

```

instead of

```python
for link in get_all_links():
    if link.followed:
        continue
    ...

```

That first version reads more compactly and arguably more clearly, yet when you’re handling a great many link objects you’d be forced into the second version so as not to hold every link object in memory all at once.

Generator expressions behave much like list comprehensions, except they skip building the whole list; what they hand you instead is a generator that yields its elements one at a time. You could rewrite the earlier example like so:

```python
links = (link for link in get_all_links() if not link.followed)
for link in links:
    ...

```

You must always enclose generator expressions in parentheses, just like the example above shows. Parentheses that mark a function call count too, so when you’d like to build an iterator that goes straight into a function call you can write:

```python
print sum(obj.count for obj in list_all_objects())

```

There are a few minor respects in which generator expressions and list comprehensions part ways. The biggest one: the loop variable (*obj* in the example above) can’t be reached anywhere beyond the generator expression itself. With list comprehensions the variable stays bound to whatever its final value was; upcoming Python releases will alter this so that list comprehensions line up with generator expressions on this point.

See also

[**PEP 289**](https://peps.python.org/pep-0289/) - Generator Expressions

The proposal came from Raymond Hettinger and was built by Jiwon Seo, with Hye-Shik Chang guiding the early work.

[Subject index](INDEX.md) · [Previous source section](pep-237-unifying-long-integers-and-integers.md) · [Next source section](pep-292-simpler-string-substitutions.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)

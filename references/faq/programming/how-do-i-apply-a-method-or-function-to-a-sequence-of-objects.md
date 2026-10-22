# How do I apply a method or function to a sequence of objects?

### How do I apply a method or function to a sequence of objects?

To invoke a method or function and collect the returned values into a list, a [list comprehension](https://docs.python.org/3.14/glossary.html#term-list-comprehension) offers an elegant answer:

```python
result = [obj.method() for obj in mylist]

result = [function(obj) for obj in mylist]

```

To merely execute the method or function without keeping the returned values, a plain [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop is enough:

```python
for obj in mylist:
    obj.method()

for obj in mylist:
    function(obj)

```

[Subject index](INDEX.md)

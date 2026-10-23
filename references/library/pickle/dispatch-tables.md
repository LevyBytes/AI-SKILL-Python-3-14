# pickle - Dispatch Tables

### Dispatch Tables

When you want to tailor the pickling of certain classes without upsetting other code that relies on pickling, you can build a pickler that carries a private dispatch table.

The [`copyreg`](https://docs.python.org/3.14/library/copyreg.html#module-copyreg) module's global dispatch table is exposed as `copyreg.dispatch_table`. So one option is to base a private dispatch table on a modified copy of `copyreg.dispatch_table`.

For example

```python
f = io.BytesIO()
p = pickle.Pickler(f)
p.dispatch_table = copyreg.dispatch_table.copy()
p.dispatch_table[SomeClass] = reduce_SomeClass

```

produces a `pickle.Pickler` instance whose private dispatch table treats the `SomeClass` class specially. As an alternative, the code

```python
class MyPickler(pickle.Pickler):
    dispatch_table = copyreg.dispatch_table.copy()
    dispatch_table[SomeClass] = reduce_SomeClass
f = io.BytesIO()
p = MyPickler(f)

```

accomplishes the same thing, except that every `MyPickler` instance shares the private dispatch table by default. By contrast, the code

```python
copyreg.pickle(SomeClass, reduce_SomeClass)
f = io.BytesIO()
p = pickle.Pickler(f)

```

alters the global dispatch table that every user of the [`copyreg`](https://docs.python.org/3.14/library/copyreg.html#module-copyreg) module shares.

[Subject index](INDEX.md) · [Previous](persistence-of-external-objects-code-example-import-pickle.md) · [Continue](handling-stateful-objects.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)

# unittest.mock - Where to patch

### Where to patch

`patch()` operates by (temporarily) swapping the object a *name* refers to for a different one. A single object can have many names pointing at it, so for the patch to work you must be sure you patch the name the system under test actually uses.

The core idea is that you patch at the spot where an object is *looked up*, which won't always coincide with where it's defined. A couple of examples make this clearer.

Picture a project we wish to test, laid out like so:

```python
a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass

```

Suppose we want to test `some_function` while mocking out `SomeClass` via `patch()`. The trouble is that importing module b — which we must, since it imports `SomeClass` from module a. Were we to use `patch()` on `a.SomeClass`, our test would see no effect; module b already holds a reference to the *real* `SomeClass`, so it appears the patching achieved nothing.

What matters is patching `SomeClass` at its point of use (or of lookup). Here `some_function` actually resolves `SomeClass` within module b, where we imported it. The patch ought to read:

```python
@patch('b.SomeClass')

```

Consider, though, the other case where module b does `import a` (rather than `from a import SomeClass`) and `some_function` references `a.SomeClass`. Both import styles see frequent use. Now the class we mean to patch is resolved inside the module, so we must patch `a.SomeClass` instead:

```python
@patch('a.SomeClass')

```

[Subject index](INDEX.md) · [Previous](nesting-patch-decorators.md) · [Continue](patching-descriptors-and-proxy-objects.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)

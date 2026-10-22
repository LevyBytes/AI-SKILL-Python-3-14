# unittest.mock — Mocking imports with patch.dict

### Mocking imports with patch.dict

Mocking gets tough in one particular spot: a local import sitting inside a function. Such imports resist mocking because they don't draw on an object from the module namespace that we could patch out.

As a rule, local imports are best steered clear of. They sometimes show up to head off circular dependencies — a problem that *usually* has a far cleaner fix (reorganize the code) — or to dodge "up front costs" by deferring the import. The latter, too, can be tackled more elegantly than with an unconditional local import (cache the module on a class or module attribute and import it only the first time it's needed).

Setting that aside, there's still a way to lean on `mock` to shape what an import returns. An import pulls an *object* out of the [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) dictionary. Bear in mind it pulls an *object*, and that object isn't required to be a module. Importing a module the first time deposits a module object into `sys.modules`, so an import normally yields a module. That, however, doesn't have to hold.

This means [`patch.dict()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch.dict) lets you slot a mock *temporarily* into [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules). While that patch holds, any import will pull the mock. Once the patch wraps up (the decorated function returns, the with block finishes, or `patcher.stop()` fires), whatever sat there beforehand is safely put back.

The following example mocks out the "fooble" module.

```python
>>> import sys
>>> mock = Mock()
>>> with patch.dict('sys.modules', {'fooble': mock}):
...    import fooble
...    fooble.blob()
...
<Mock name='mock.blob()' id='...'>
>>> assert 'fooble' not in sys.modules
>>> mock.blob.assert_called_once_with()

```

Notice that `import fooble` goes through fine, yet once we exit there is no "fooble" remaining in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

The `from module import name` variation is handled as well:

```python
>>> mock = Mock()
>>> with patch.dict('sys.modules', {'fooble': mock}):
...    from fooble import blob
...    blob.blip()
...
<Mock name='mock.blob.blip()' id='...'>
>>> mock.blob.blip.assert_called_once_with()

```

A bit of extra effort even lets you mock package imports:

```python
>>> mock = Mock()
>>> modules = {'package': mock, 'package.module': mock.module}
>>> with patch.dict('sys.modules', modules):
...    from package.module import fooble
...    fooble()
...
<Mock name='mock.module.fooble()' id='...'>
>>> mock.module.fooble.assert_called_once_with()

```

[Subject index](INDEX.md) · [Previous](mock-subclasses-and-their-attributes.md) · [Continue](tracking-order-of-calls-and-less-verbose-call-assertions.md) · [Owning module, declaration or section: unittest.mock](mock-patching-methods.md)

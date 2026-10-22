# 5.4.2. Submodules

### 5.4.2. Submodules

Whenever a submodule gets loaded through any route (for instance, the `importlib` APIs, the `import` or `import-from` statements, or the built-in `__import__()`), the parent module's namespace receives a binding pointing at the submodule object. As an illustration, suppose package `spam` contains a submodule `foo`; once `spam.foo` is imported, the attribute `foo` on `spam` will be bound to that submodule. Imagine you set up this directory layout:

```python
spam/
    __init__.py
    foo.py

```

and the file `spam/__init__.py` contains this one line:

```python
from .foo import Foo

```

then running the snippet below installs name bindings for both `foo` and `Foo` inside the `spam` module:

```python
>>> import spam
>>> spam.foo
<module 'spam.foo' from '/tmp/imports/spam/foo.py'>
>>> spam.Foo
<class 'spam.foo.Foo'>

```

Considering Python's usual name binding behaviour this may look unexpected, yet it is really a core characteristic of the import system. The guarantee that holds is this: whenever both `sys.modules['spam']` and `sys.modules['spam.foo']` exist (which is the state after the import shown above), the second one has to be reachable as the `foo` attribute of the first.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](loading.md) · [Previous source section](loaders.md) · [Following source section](module-specs.md)

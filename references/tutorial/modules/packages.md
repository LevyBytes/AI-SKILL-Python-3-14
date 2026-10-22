# 6.4. Packages

### 6.4. Packages

Packages give you a way to organize Python's module namespace through "dotted module names". For example, the module name `A.B` points to a submodule `B` living inside a package `A`. In the same way that modules spare the authors of different modules from clashing over one another's global variable names, dotted module names spare the authors of multi-module packages such as NumPy or Pillow from clashing over one another's module names.

Imagine you want to build a set of modules (a "package") for handling sound files and sound data in a consistent way. Sound files come in many formats (usually identified by their extension, such as `.wav`, `.aiff`, `.au`), so you may find yourself building and maintaining an ever-growing set of modules to convert between those formats. And there are plenty of operations you might want to apply to sound data (mixing, adding echo, applying an equalizer function, fabricating an artificial stereo effect), so on top of that you'll keep churning out modules to carry out these operations. Here's one way you might lay out your package (shown as a hierarchical filesystem):

```text
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

```

As it imports the package, Python looks through the directories on `sys.path` for the package's subdirectory.

The `__init__.py` files are needed so that Python regards a directory holding such a file as a package (unless you're using a [namespace package](https://docs.python.org/3.14/glossary.html#term-namespace-package), which is a fairly advanced feature). This stops directories with a common name, like `string`, from accidentally masking valid modules that turn up later along the module search path. At its simplest, `__init__.py` can be nothing more than an empty file, yet it can also run initialization code for the package or assign the `__all__` variable, which is covered later.

People using the package can import its individual modules, for instance:

```python
import sound.effects.echo

```

This pulls in the submodule `sound.effects.echo`. You have to refer to it by its full name.

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

```

Another way to import the submodule is:

```python
from sound.effects import echo

```

This too pulls in the submodule `echo`, and makes it reachable without the package prefix, so you can use it like this:

```python
echo.echofilter(input, output, delay=0.7, atten=4)

```

Still another variation is to import the function or variable you want directly:

```python
from sound.effects.echo import echofilter

```

Once again, this pulls in the submodule `echo`, but now it makes its function `echofilter()` directly reachable:

```python
echofilter(input, output, delay=0.7, atten=4)

```

Bear in mind that with `from package import item`, the item may be a submodule (or subpackage) of the package, or it may be some other name the package defines, such as a function, class, or variable. The `import` statement first checks whether the item is defined within the package; if it isn't, it presumes the item is a module and tries to load it. Should that loading fail, an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) exception gets raised.

By contrast, with syntax of the form `import item.subitem.subsubitem`, each item apart from the final one has to be a package; the final item may be a module or a package but cannot be a class, function, or variable defined inside the preceding item.

[Subject index](INDEX.md) · [Previous source section](the-dir-function.md) · [Following source section](importing-from-a-package.md)

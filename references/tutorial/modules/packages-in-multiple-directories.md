# 6.4.3. Packages in Multiple Directories

### 6.4.3. Packages in Multiple Directories

There is yet another special attribute that packages carry, namely [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__). At setup time it holds a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) of strings naming the folder where the package’s `__init__.py` lives, established before that file’s code ever runs. You are free to alter this variable, and when you do, it reshapes how later lookups for modules and subpackages inside the package proceed.

Although you will rarely have call for this capability, it does let you broaden the collection of modules that a package exposes.

Footnotes

[Subject index](INDEX.md) · [Previous source section](intra-package-references.md)

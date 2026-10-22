# What’s New In Python 3.12 / zipimport — zipimport

### zipimport

- Drop the `find_loader()` along with `find_module()` methods of [`zipimport`](https://docs.python.org/3.14/library/zipimport.html#module-zipimport), which were deprecated in Python 3.10; reach for `find_spec()` in their place. The reasoning is laid out in [**PEP 451**](https://peps.python.org/pep-0451/). (Contributed by Victor Stinner in [gh-94379](https://github.com/python/cpython/issues/94379).)

[Subject index](INDEX.md) · [Previous source section](xml-etree-elementtree.md) · [Next source section](others.md) · [Release/subject declaration](summary-release-highlights.md)

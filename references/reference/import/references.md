# 5.9. References

### 5.9. References

Over the years the import machinery has changed a great deal from how it stood in Python’s earliest days. You can still read the original [specification for packages](https://www.python.org/doc/essays/packages/), though a few particulars have shifted in the time since it was written.

What first specified [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) was [**PEP 302**](https://peps.python.org/pep-0302/), later broadened by [**PEP 420**](https://peps.python.org/pep-0420/).

[**PEP 420**](https://peps.python.org/pep-0420/) brought [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package) to Python 3.3. On top of that, [**PEP 420**](https://peps.python.org/pep-0420/) added the `find_loader()` protocol to stand in for `find_module()`.

[**PEP 366**](https://peps.python.org/pep-0366/) lays out how the `__package__` attribute was introduced so that main modules could perform explicit relative imports.

[**PEP 328**](https://peps.python.org/pep-0328/) ushered in both absolute imports and explicit relative ones, and at first put forward `__name__` to carry the semantics that [**PEP 366**](https://peps.python.org/pep-0366/) would in the end pin to `__package__`.

[**PEP 338**](https://peps.python.org/pep-0338/) spells out running modules as though they were scripts.

[**PEP 451**](https://peps.python.org/pep-0451/) wraps each module’s import state up inside spec objects. Beyond that, it shifts the bulk of the loaders’ boilerplate duties back over to the import machinery. Thanks to these revisions, a number of APIs throughout the import system could be deprecated, while fresh methods were granted to finders and loaders.

Footnotes

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Previous source section](main-spec.md)

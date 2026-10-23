# What's New In Python 3.4 / PEP 436: Argument Clinic - inspect, pydoc

### PEP 436: Argument Clinic

"Argument Clinic" ([**PEP 436**](https://peps.python.org/pep-0436/)) has become a piece of the CPython build pipeline and helps streamline how accurate signatures get defined and maintained for builtins as well as standard library extension modules written in C.

A handful of standard library extension modules were ported over to Argument Clinic during Python 3.4, with [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) and [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) revised to match.

The expectation is that signature metadata supporting programmatic introspection will land on further C-implemented callables across the Python 3.4 maintenance releases.

Note

The Argument Clinic PEP has not been kept fully current with where the implementation stands. The release manager and the core development team judged that tolerable here, given that Argument Clinic won't be exposed as a public API for outside parties to use in Python 3.4.

See also

[**PEP 436**](https://peps.python.org/pep-0436/) ? The Argument Clinic DSL

PEP written and implemented by Larry Hastings.

[Subject index](INDEX.md) · [Previous source section](pep-456-secure-and-interchangeable-hash-algorithm.md) · [Next source section](other-build-and-c-api-changes.md) · [Release/subject declaration](release-highlights.md)

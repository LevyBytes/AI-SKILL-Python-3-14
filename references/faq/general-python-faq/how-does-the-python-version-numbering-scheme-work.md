# How does the Python version numbering scheme work?

### How does the Python version numbering scheme work?

The numbering for Python releases takes the form "A.B.C" or "A.B":

- *A* denotes the major version — it advances only when the language undergoes truly major changes.

- *B* denotes the minor version — it advances for changes of a less momentous kind.

- *C* denotes the micro version — it advances with every bugfix release.

Bugfix releases don't account for every release. As a new feature release approaches, several development releases appear, tagged alpha, beta, or release candidate. Alphas land early, before interfaces have settled, so an interface shifting from one alpha to the next is hardly surprising. Betas hold steady more, keeping current interfaces intact while perhaps introducing new modules, and release candidates are locked, altering nothing apart from fixes demanded by critical bugs.

A further suffix marks alpha, beta, and release candidate versions:

- An alpha version carries the suffix "aN" for some small number *N*.

- A beta version carries the suffix "bN" for some small number *N*.

- A release candidate carries the suffix "rcN" for some small number *N*.

Put differently, every version tagged *2.0aN* comes before the ones tagged *2.0bN*, which come before those tagged *2.0rcN*, and *those* come before 2.0.

Version numbers ending in a "+" may also turn up, such as "2.2+". Such versions are unreleased, compiled straight from the CPython development repository. Typically, once a final minor release ships, the version steps up to the next minor version, becoming the "a0" version — for instance, "2.4a0".

Consult the [Developer's Guide](https://devguide.python.org/developer-workflow/development-cycle/) for further detail on the development cycle, and [**PEP 387**](https://peps.python.org/pep-0387/) for more on Python's backward compatibility policy. Refer as well to the documentation on [`sys.version`](https://docs.python.org/3.14/library/sys.html#sys.version), [`sys.hexversion`](https://docs.python.org/3.14/library/sys.html#sys.hexversion), and [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info).

[Subject index](INDEX.md)

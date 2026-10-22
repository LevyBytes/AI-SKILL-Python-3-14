# Python 3.9.0 alpha 6 / core and builtins / compiler and parser

[bpo-40334](https://bugs.python.org/issue?@action=redirect&bpo=40334): Move over to a fresh parser grounded in PEG. Consult PEP 617 for the full story. Should you need the old parser back for now, pass `-X oldparser` or set `PYTHONOLDPARSER=1`. Within Python 3.10 the old parser disappears entirely, taking the already-deprecated `parser` module and everything resting on it.

[bpo-40141](https://bugs.python.org/issue?@action=redirect&bpo=40141): Attach column plus line data onto `ast.keyword` nodes. Pablo Galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

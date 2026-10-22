# Python 3.5.2 release candidate 1 / library / traceback

[bpo-14285](https://bugs.python.org/issue?@action=redirect&bpo=14285): Running a package through the "python -m package" form now produces a correct traceback when that package's initialization breaks. Rather than turning such a failure into ImportError, the "runpy" module forwards exceptions raised during package initialization straight to whoever called it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

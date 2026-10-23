# What's New In Python 3.3 / Using importlib as the Implementation of Import - importlib

### Using importlib as the Implementation of Import

> [bpo-2377](https://bugs.python.org/issue?@action=redirect&bpo=2377) - Replace __import__ w/ importlib.__import__ [bpo-13959](https://bugs.python.org/issue?@action=redirect&bpo=13959) - Re-implement parts of `imp` in pure Python [bpo-14605](https://bugs.python.org/issue?@action=redirect&bpo=14605) - Make import machinery explicit [bpo-14646](https://bugs.python.org/issue?@action=redirect&bpo=14646) - Require loaders set __loader__ and __package__

Behind the [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function now sits [`importlib.__import__()`](https://docs.python.org/3.14/library/importlib.html#importlib.__import__). With this, “phase 2” of [**PEP 302**](https://peps.python.org/pep-0302/) reaches its conclusion. Several gains follow from the switch. To begin with, much of the machinery driving import is now surfaced rather than staying buried implicitly inside the C code. Furthermore, every Python VM that supports Python 3.3 can share one common implementation, which helps put a stop to VM-specific divergence in how import behaves. Lastly, maintaining import becomes simpler, leaving room for later expansion.

Ordinary users ought to see no shift in semantics whatsoever. If your code currently reaches into import or invokes it programmatically, the Porting Python code portion of this document describes the edits you may need to make.

[Subject index](INDEX.md) · [Previous source section](simplenamespace-end.md) · [Next source section](new-apis.md) · [Release/subject declaration](summary-release-highlights.md)

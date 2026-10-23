# What's New In Python 3.9 / New Parser - ast

### New Parser

A fresh parser ships in Python 3.9, grounded in [PEG](https://en.wikipedia.org/wiki/Parsing_expression_grammar) rather than [LL(1)](https://en.wikipedia.org/wiki/LL_parser). Throughput of the replacement parser sits roughly on par with the prior one, yet the PEG approach affords greater latitude than LL(1) for crafting fresh language constructs. That latitude gets exercised beginning in Python 3.10 and onward.

The [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module runs on the replacement parser and emits the very same AST that the prior parser did.

Come Python 3.10, the prior parser disappears together with everything relying on it (chiefly the long-deprecated `parser` module). Within Python 3.9 *only*, a command line switch (`-X oldparser`) or an environment variable (`PYTHONOLDPARSER=1`) reverts you to the LL(1) parser.

Consult [**PEP 617**](https://peps.python.org/pep-0617/) for further detail. (Contributed by Guido van Rossum, Pablo Galindo and Lysandros Nikolaou in [bpo-40334](https://bugs.python.org/issue?@action=redirect&bpo=40334).)

[Subject index](INDEX.md) · [Previous source section](type-hinting-generics-in-standard-collections.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)

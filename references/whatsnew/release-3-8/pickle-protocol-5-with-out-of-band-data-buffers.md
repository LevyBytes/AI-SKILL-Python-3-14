# What’s New In Python 3.8 / Pickle protocol 5 with out-of-band data buffers - pickle

### Pickle protocol 5 with out-of-band data buffers

Whenever [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) ships sizeable data across Python processes so as to exploit multiple cores or several machines, getting the transfer fast matters — that means cutting down on memory copies and, where it helps, leaning on bespoke tricks such as compression tuned to the data.

Protocol 5 of [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) adds out-of-band buffer handling, in which [**PEP 3118**](https://peps.python.org/pep-3118/)-compatible data may travel apart from the main pickle stream whenever the communication layer chooses.

A complete write-up appears in [**PEP 574**](https://peps.python.org/pep-0574/).

(Antoine Pitrou contributed this in [bpo-36785](https://bugs.python.org/issue?@action=redirect&bpo=36785).)

[Subject index](INDEX.md) · [Previous source section](pep-590-vectorcall-a-fast-calling-protocol-for-cpython.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](assignment-expressions.md)

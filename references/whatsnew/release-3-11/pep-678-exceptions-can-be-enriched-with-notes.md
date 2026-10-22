# What's New In Python 3.11 / PEP 678: Exceptions can be enriched with notes

> (Contributed by Irit Katriel in [bpo-45292](https://bugs.python.org/issue?@action=redirect&bpo=45292). PEP written by Irit Katriel, Yury Selivanov and Guido van Rossum.)

### PEP 678: Exceptions can be enriched with notes

A new [`add_note()`](https://docs.python.org/3.14/library/exceptions.html#BaseException.add_note) method lands on [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException). Use it to attach contextual detail to an exception that was not on hand at the moment the exception was originally raised. Whatever notes you add then show up in the standard traceback.

Consult [**PEP 678**](https://peps.python.org/pep-0678/) for the full treatment.

[Subject index](INDEX.md) · [Previous source section](pep-654-exception-groups-and-except.md) · [Next source section](windows-py-exe-launcher-improvements.md) · [Release/subject declaration](summary-release-highlights.md)

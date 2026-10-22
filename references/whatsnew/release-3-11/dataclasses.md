# What's New In Python 3.11 / dataclasses

### dataclasses

- The mutability test for field defaults was revised so that only [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) defaults pass, rather than accepting any object that is not a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) instance. (Contributed by Eric V. Smith in [bpo-44674](https://bugs.python.org/issue?@action=redirect&bpo=44674).)

[Subject index](INDEX.md) · [Previous source section](contextlib.md) · [Next source section](datetime.md) · [Release/subject declaration](summary-release-highlights.md)

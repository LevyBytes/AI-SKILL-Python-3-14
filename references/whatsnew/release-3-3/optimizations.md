# What's New In Python 3.3 / Optimizations

### Optimizations

Substantial speed gains were introduced:

- Owing to [**PEP 393**](https://peps.python.org/pep-0393/), several Unicode string operations were sped up:

  - depending on the text, memory usage shrinks by a factor of 2 to 4

  - encoding an ASCII string to UTF-8 no longer touches the characters, since the UTF-8 form is shared with the ASCII form

  - the UTF-8 encoder has been optimized

  - repeating one ASCII letter, and slicing a substring out of an ASCII string, runs 4 times faster

- UTF-8 runs at 2x to 4x its former speed; UTF-16 encoding climbs to as much as 10x faster.

Serhiy Storchaka contributed this ? see [bpo-14624](https://bugs.python.org/issue?@action=redirect&bpo=14624), [bpo-14738](https://bugs.python.org/issue?@action=redirect&bpo=14738) and [bpo-15026](https://bugs.python.org/issue?@action=redirect&bpo=15026).

[Subject index](INDEX.md) · [Previous source section](zlib.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](summary-release-highlights.md)

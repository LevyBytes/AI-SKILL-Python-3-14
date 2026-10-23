# What's New In Python 3.13 / optparse - argparse

### optparse

- This module no longer counts as [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) stays the recommended pick for new projects that skip a third party command line argument processing library, yet certain traits of how `argparse` operates mean the lower level `optparse` module can serve as a sturdier base for *writing* argument processing libraries, and for building command line applications that follow, more rigidly than `argparse` does, the various Unix command line processing conventions rooted in how the C `getopt()` function behaves . (Contributed by Alyssa Coghlan and Serhiy Storchaka in [gh-126180](https://github.com/python/cpython/issues/126180).)

[Subject index](INDEX.md) · [Previous source section](opcode.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)

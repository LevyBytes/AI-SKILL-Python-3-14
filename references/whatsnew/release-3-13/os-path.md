# What's New In Python 3.13 / os.path - os.path

### os.path

- A new [`isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved) tells you whether a given path is reserved on this system. Only Windows offers this function. (Contributed by Barney Gale in [gh-88569](https://github.com/python/cpython/issues/88569).)

- Under Windows, [`isabs()`](https://docs.python.org/3.14/library/os.path.html#os.path.isabs) stops treating a path that opens with just one slash (`\` or `/`) as absolute. (Contributed by Barney Gale and Jon Foster in [gh-44626](https://github.com/python/cpython/issues/44626).)

- Even for an inaccessible file, [`realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) now resolves MS-DOS style file names. (Contributed by Moonsik Park in [gh-82367](https://github.com/python/cpython/issues/82367).)

[Subject index](INDEX.md) · [Previous source section](os.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)

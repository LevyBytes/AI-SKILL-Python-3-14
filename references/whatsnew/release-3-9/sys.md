# What's New In Python 3.9 / sys — sys

### sys

A new [`sys.platlibdir`](https://docs.python.org/3.14/library/sys.html#sys.platlibdir) attribute was added: it holds the name of the platform-specific library directory. This name helps assemble the standard library path together with the locations of installed extension modules. On the majority of platforms its value is `"lib"`. Under Fedora and SuSE, 64-bit platforms set it to `"lib64"`. (Contributed by Jan Matějek, Matěj Cepl, Charalampos Stratakis and Victor Stinner in [bpo-1294959](https://bugs.python.org/issue?@action=redirect&bpo=1294959).)

In earlier releases, [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) used block buffering whenever it was non-interactive. From now on `stderr` is line-buffered by default in every case. (Contributed by Jendrik Seipp in [bpo-13601](https://bugs.python.org/issue?@action=redirect&bpo=13601).)

[Subject index](INDEX.md) · [Previous source section](time.md) · [Next source section](tracemalloc.md) · [Release/subject declaration](summary-release-highlights.md)

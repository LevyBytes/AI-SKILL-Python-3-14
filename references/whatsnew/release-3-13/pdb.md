# What's New In Python 3.13 / pdb — pdb, sys, zipapp

### pdb

- Now [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) and [`set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace) drop into the debugger right away instead of waiting for the following line to run. The adjustment keeps the debugger from breaking outside the context whenever `breakpoint()` sits at a context's tail. (Contributed by Tian Gao in [gh-118579](https://github.com/python/cpython/issues/118579).)

- While [`sys.flags.safe_path`](https://docs.python.org/3.14/library/sys.html#sys.flags.safe_path) is active, `sys.path[0]` no longer gets swapped for the folder holding the script under debugging. (Contributed by Tian Gao and Christian Walther in [gh-111762](https://github.com/python/cpython/issues/111762).)

- A [`zipapp`](https://docs.python.org/3.14/library/zipapp.html#module-zipapp) can now serve as a debugging target. (Contributed by Tian Gao in [gh-118501](https://github.com/python/cpython/issues/118501).)

- During post-mortem debugging, [`pm()`](https://docs.python.org/3.14/library/pdb.html#pdb.pm) gains the option to walk among chained exceptions through the new [`exceptions [exc_number]`](https://docs.python.org/3.14/library/pdb.html#pdbcommand-exceptions) command for Pdb. (Contributed by Matthias Bussonnier in [gh-106676](https://github.com/python/cpython/issues/106676).)

- Statements and expressions that begin with a pdb command are now recognized and run correctly. (Contributed by Tian Gao in [gh-108464](https://github.com/python/cpython/issues/108464).)

[Subject index](INDEX.md) · [Previous source section](pathlib.md) · [Next source section](queue.md) · [Release/subject declaration](summary-release-highlights.md)

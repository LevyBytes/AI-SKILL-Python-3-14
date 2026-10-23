# What's New In Python 3.4 / pdb - asyncio, pdb

### pdb

[`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) was improved to deal with generators, [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield), and `yield from` in a far handier way. That proves particularly useful while debugging [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) based programs. (Contributed by Andrew Svetlov and Xavier de Gaye in [bpo-16596](https://bugs.python.org/issue?@action=redirect&bpo=16596).)

The `print` command was dropped from [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb), giving back access to the Python [`print()`](https://docs.python.org/3.14/library/functions.html#print) function at the pdb command line. The Python2 `pdb` carried no `print` command; typing `print` there ran the `print` statement instead. Within Python3 `print` had been turned, by error, into an alias for the pdb [`p`](https://docs.python.org/3.14/library/pdb.html#pdbcommand-p) command. `p`, though, shows the `repr` of its argument rather than the `str` that the Python2 `print` command produced. Even worse, the Python3 `pdb print` command masked the Python3 `print` function, leaving it unreachable from the `pdb` prompt. (Contributed by Connor Osborn in [bpo-18764](https://bugs.python.org/issue?@action=redirect&bpo=18764).)

[Subject index](INDEX.md) · [Previous source section](os.md) · [Next source section](pickle.md) · [Release/subject declaration](release-highlights.md)

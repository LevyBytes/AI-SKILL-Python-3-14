# Python 3.14.1 final / library / readline

[gh-140398](https://github.com/python/cpython/issues/140398): Resolve memory leaks across the [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) functions [`read_init_file()`](https://docs.python.org/3.14/library/readline.html#readline.read_init_file), [`read_history_file()`](https://docs.python.org/3.14/library/readline.html#readline.read_history_file), [`write_history_file()`](https://docs.python.org/3.14/library/readline.html#readline.write_history_file), plus [`append_history_file()`](https://docs.python.org/3.14/library/readline.html#readline.append_history_file) whenever [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) fails.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

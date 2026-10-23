# What's New In Python 3.11 / Misc - re

### Misc

- Thanks to namespaces that objects build lazily, instances consume less memory, and the dictionaries backing those namespaces now share their keys more readily as well. (Contributed Mark Shannon in [bpo-45340](https://bugs.python.org/issue?@action=redirect&bpo=45340) and [bpo-40116](https://bugs.python.org/issue?@action=redirect&bpo=40116).)

- So-called “Zero-cost” exceptions arrived, so a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement carries no overhead whenever nothing is raised. (Contributed by Mark Shannon in [bpo-40222](https://bugs.python.org/issue?@action=redirect&bpo=40222).)

- By packing exceptions inside the interpreter more compactly, the work needed to catch one dropped roughly 10%. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

- The matching engine behind [`re`](https://docs.python.org/3.14/library/re.html#module-re) saw a partial rewrite and now leans on computed gotos (also called “threaded code”) wherever the platform allows. Consequently, the [pyperformance regular expression benchmarks](https://pyperformance.readthedocs.io/benchmarks.html#regex-dna) run as much as 10% quicker under Python 3.11 than they did on Python 3.10. (Contributed by Brandt Bucher in [gh-91404](https://github.com/python/cpython/issues/91404).)

[Subject index](INDEX.md) · [Previous source section](faster-runtime-pep-659-specializing-adaptive-interpreter.md) · [Next source section](faq-how-should-i-write-my-code-to-utilize-these-speedups.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.6 / tracemalloc - tracemalloc

### tracemalloc

Tracing memory allocations spread over several distinct address spaces is now possible with the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module.

To screen block traces according to their address space (domain), the fresh [`DomainFilter`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.DomainFilter) filter class was introduced.

(Contributed by Victor Stinner in [bpo-26588](https://bugs.python.org/issue?@action=redirect&bpo=26588).)

[Subject index](INDEX.md) · [Previous source section](traceback.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](typing.md)

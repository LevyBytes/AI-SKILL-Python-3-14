# What's New In Python 3.7 / types - types

### types

Four fresh classes can now be used: [`WrapperDescriptorType`](https://docs.python.org/3.14/library/types.html#types.WrapperDescriptorType), [`MethodWrapperType`](https://docs.python.org/3.14/library/types.html#types.MethodWrapperType), [`MethodDescriptorType`](https://docs.python.org/3.14/library/types.html#types.MethodDescriptorType), and [`ClassMethodDescriptorType`](https://docs.python.org/3.14/library/types.html#types.ClassMethodDescriptorType). (Work by Manuel Krebber along with Guido van Rossum landed in [bpo-29377](https://bugs.python.org/issue?@action=redirect&bpo=29377); Serhiy Storchaka added more in [bpo-32265](https://bugs.python.org/issue?@action=redirect&bpo=32265).)

Following the scheme of [**PEP 560**](https://peps.python.org/pep-0560/), the freshly added [`types.resolve_bases()`](https://docs.python.org/3.14/library/types.html#types.resolve_bases) function dynamically resolves MRO entries. (Contributed by Ivan Levkivskyi in [bpo-32717](https://bugs.python.org/issue?@action=redirect&bpo=32717).)

[Subject index](INDEX.md) · [Previous source section](tracemalloc.md) · [Next source section](unicodedata.md) · [Release/subject declaration](summary-release-highlights.md)

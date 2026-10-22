# What's New In Python 3.4 / wave — wave

### wave

The [`getparams()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getparams) method hands back a namedtuple these days in place of a bare tuple. (Contributed by Claudiu Popa in [bpo-17487](https://bugs.python.org/issue?@action=redirect&bpo=17487).)

[`wave.open()`](https://docs.python.org/3.14/library/wave.html#wave.open) has gained support for the context management protocol. (Contributed by Claudiu Popa in [bpo-17616](https://bugs.python.org/issue?@action=redirect&bpo=17616).)

[`wave`](https://docs.python.org/3.14/library/wave.html#module-wave) is now able to [write output to unseekable files](https://docs.python.org/3.14/library/wave.html#wave-write-objects). (Contributed by David Jones, Guilherme Polo, and Serhiy Storchaka in [bpo-5202](https://bugs.python.org/issue?@action=redirect&bpo=5202).)

The [`writeframesraw()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write.writeframesraw) plus [`writeframes()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write.writeframes) methods will now take any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311).)

[Subject index](INDEX.md) · [Previous source section](venv.md) · [Next source section](weakref.md) · [Release/subject declaration](release-highlights.md)

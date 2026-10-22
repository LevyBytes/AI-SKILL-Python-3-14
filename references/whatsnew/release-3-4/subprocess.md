# What's New In Python 3.4 / subprocess — subprocess

### subprocess

[`check_output()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.check_output) now takes an *input* argument by which you can feed the `stdin` contents to the command being executed. (Contributed by Zack Weinberg in [bpo-16624](https://bugs.python.org/issue?@action=redirect&bpo=16624).)

[`getoutput()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.getoutput) and [`getstatusoutput()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.getstatusoutput) now function under Windows. That change had in fact slipped in unintentionally back in 3.3.4. (Contributed by Tim Golden in [bpo-10197](https://bugs.python.org/issue?@action=redirect&bpo=10197).)

[Subject index](INDEX.md) · [Previous source section](struct.md) · [Next source section](sunau.md) · [Release/subject declaration](release-highlights.md)

# What's New In Python 3.10 / fileinput - fileinput, io

### fileinput

Add *encoding* and *errors* parameters to [`fileinput.input()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.input) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput). (Contributed by Inada Naoki in [bpo-43712](https://bugs.python.org/issue?@action=redirect&bpo=43712).)

When *mode* is “r” and the file is compressed, [`fileinput.hook_compressed()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.hook_compressed) now hands back a [`TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) object, matching how uncompressed files behave. (Contributed by Inada Naoki in [bpo-5758](https://bugs.python.org/issue?@action=redirect&bpo=5758).)

[Subject index](INDEX.md) · [Previous source section](enum.md) · [Next source section](faulthandler.md) · [Release/subject declaration](summary-release-highlights.md)

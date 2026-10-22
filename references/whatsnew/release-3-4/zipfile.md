# What's New In Python 3.4 / zipfile — zipfile

### zipfile

The [`writepy()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.PyZipFile.writepy) method belonging to the [`PyZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.PyZipFile) class gained a fresh *filterfunc* option, letting you steer which directories and files get pulled into the archive. As one use, you might keep test files out of the archive with it. (Contributed by Christian Tismer in [bpo-19274](https://bugs.python.org/issue?@action=redirect&bpo=19274).)

The *allowZip64* parameter handed to [`ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile) and [`PyZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.PyZipFile) now defaults to `True`. (Contributed by William Mallard in [bpo-17201](https://bugs.python.org/issue?@action=redirect&bpo=17201).)

[Subject index](INDEX.md) · [Previous source section](xml-etree.md) · [Next source section](pep-445-customization-of-cpython-memory-allocators.md) · [Release/subject declaration](release-highlights.md)

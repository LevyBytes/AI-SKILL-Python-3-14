# Python 3.11.0 alpha 1 / library / files and paths

[bpo-44539](https://bugs.python.org/issue?@action=redirect&bpo=44539): Recognition of JPEG files lacking JFIF or Exif markers is now supported.

[bpo-44439](https://bugs.python.org/issue?@action=redirect&bpo=44439): A fix landed in the `bz2.BZ2File.write()` and `lzma.LZMAFile.write()` methods: where input data is an object supporting the buffer protocol, the reported file length could come out wrong.

[bpo-45371](https://bugs.python.org/issue?@action=redirect&bpo=45371): Resolved a clang rpath problem inside `distutils`. The UnixCCompiler now passes the proper clang option for adding a runtime library directory (rpath) onto a shared library.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

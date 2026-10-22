# What’s New In Python 3.5 / New `make regen-all` build target

### Notable changes in Python 3.5.4

### New `make regen-all` build target

With the aim of making cross-compilation easier and of ensuring CPython can be compiled reliably even when no prior Python build is present, the autotools-based build system has given up automatically rebuilding generated files according to their file modification times.

A new `make regen-all` command was introduced in its stead, forcing those files to be regenerated whenever you ask for it (say, after a first Python build has already been produced from the pregenerated versions).

There are narrower regeneration targets too - look at [Makefile.pre.in](https://github.com/python/cpython/tree/3.14/Makefile.pre.in) for specifics.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 3.5.4.

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-5-changes-in-the-c-api.md) · [Next source section](removal-of-make-touch-build-target.md) · [Release/subject declaration](summary-release-highlights.md)

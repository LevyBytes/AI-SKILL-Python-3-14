# What’s New in Python 2.7 / New `make regen-all` build target

### New `make regen-all` build target

So as to ease cross-compilation and to guarantee that CPython can be built dependably without an already-installed Python being on hand, the autotools-driven build system has stopped trying to silently rebuild generated files from their file modification times.

In its place, a new `make regen-all` command was added to compel regeneration of those files on demand (for instance, once an initial Python has already been built from the pregenerated versions).

Finer-grained regeneration targets exist as well - consult [Makefile.pre.in](https://github.com/python/cpython/tree/3.14/Makefile.pre.in) for the details.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 2.7.14.

[Subject index](INDEX.md) · [Previous source section](pep-493-https-verification-migration-tools-for-python-2-7.md) · [Next source section](removal-of-make-touch-build-target.md) · [Release/subject declaration](the-future-for-python-2-x.md)

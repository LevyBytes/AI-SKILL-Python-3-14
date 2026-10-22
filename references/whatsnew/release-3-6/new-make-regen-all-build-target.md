# What's New In Python 3.6 / New `make regen-all` build target

So that cross-compilation gets easier — and so CPython can be built dependably even when no prior Python install is on hand — the autotools-driven build system has stopped silently rebuilding generated files by comparing their modification timestamps.

In its place sits a fresh `make regen-all` command that, on demand, drives those files to be regenerated (for instance, once an early Python has been compiled from the pregenerated copies).

There are narrower regeneration targets defined as well — consult [Makefile.pre.in](https://github.com/python/cpython/tree/3.14/Makefile.pre.in) for the specifics.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 3.6.2.

[Subject index](INDEX.md) · [Next source section](removal-of-make-touch-build-target.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](bytecode-migration-changes.md) · [Preceding release/subject continuation](bytecode-migration-changes.md)

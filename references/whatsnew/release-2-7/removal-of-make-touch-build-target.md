# What’s New in Python 2.7 / Removal of `make touch` build target

### Removal of `make touch` build target

The `make touch` build target, which formerly asked for silent regeneration of generated files by refreshing their modification times, is gone.

The new `make regen-all` target now takes its place.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 2.7.14.

[Subject index](INDEX.md) · [Previous source section](new-make-regen-all-build-target.md) · [Release/subject declaration](the-future-for-python-2-x.md)

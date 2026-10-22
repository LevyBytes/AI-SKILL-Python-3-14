# What’s New In Python 3.5 / Removal of `make touch` build target

### Removal of `make touch` build target

Formerly the `make touch` build target served to request automatic regeneration of generated files by bumping their modification times; it has now been taken out.

Its replacement is the new `make regen-all` target.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 3.5.4.

[Subject index](INDEX.md) · [Previous source section](new-make-regen-all-build-target.md) · [Release/subject declaration](summary-release-highlights.md)

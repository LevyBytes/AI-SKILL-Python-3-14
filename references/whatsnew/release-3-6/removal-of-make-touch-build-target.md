# What's New In Python 3.6 / Removal of `make touch` build target

### Removal of `make touch` build target

That `make touch` build target — which formerly triggered implicit regeneration of generated files by bumping their modification times — is now gone.

Taking its place is the new `make regen-all` target.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 3.6.2.

[Subject index](INDEX.md) · [Previous source section](new-make-regen-all-build-target.md) · [Next source section](notable-changes-in-python-3-6-4.md) · [Release/subject declaration](summary-release-highlights.md)

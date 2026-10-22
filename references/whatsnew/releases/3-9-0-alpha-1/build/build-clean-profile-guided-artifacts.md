# Python 3.9.0 alpha 1 / build / adjust clean makefile target also wipes program guided optimization

[bpo-37725](https://bugs.python.org/issue?@action=redirect&bpo=37725): Adjust the "clean" makefile target so it also wipes the program guided optimization (PGO) data. Previously this required running "make clean" plus "make profile-removal", or else "make clobber".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

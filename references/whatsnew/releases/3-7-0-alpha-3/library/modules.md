# Python 3.7.0 alpha 3 / library / modules

[bpo-31985](https://bugs.python.org/issue?@action=redirect&bpo=31985): Officially deprecates aifc.openfp, sunau.openfp, and wave.openfp. Ever since change 7bc817d5ba917528e8bd07ec461c635291e7b06a back in 1993, openfp in each of those three modules had pointed at that module's open function purely for backwards compatibility, though it had stayed both untested and undocumented.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.10.0 alpha 3 / library / multiprocessing

[bpo-42406](https://bugs.python.org/issue?@action=redirect&bpo=42406): A defect in `pickle.whichmodule` was corrected: importing `multiprocessing` could alter how pickle decides which module owns an object, which risked breaking the unpickling of such objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

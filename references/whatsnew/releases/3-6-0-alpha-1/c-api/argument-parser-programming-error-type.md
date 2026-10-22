# Python 3.6.0 alpha 1 / c api / every programming bug involving pyarg parsetupleandkeywords raises systemerror

[bpo-26312](https://bugs.python.org/issue?@action=redirect&bpo=26312): Every programming bug involving PyArg_ParseTupleAndKeywords() now raises SystemError. Some of those programming bugs used to raise RuntimeError instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

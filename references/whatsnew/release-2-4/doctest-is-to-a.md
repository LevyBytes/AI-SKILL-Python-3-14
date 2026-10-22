# Python 2.4 changes: Doctest unified-diff output

Run that function's tests with [`doctest.REPORT_UDIFF`](https://docs.python.org/3.14/library/doctest.html#doctest.REPORT_UDIFF) in effect and the output you see is:

```none
**********************************************************************
File "t.py", line 15, in g
Failed example:
    g(4)
Differences (unified diff with -expected +actual):
    @@ -2,3 +2,3 @@
     is
     a
    -lengthy
    +rather
**********************************************************************

```

[Subject index](INDEX.md) · [Previous source section](doctest-f-and-o-and-p-and-g.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Release/subject declaration](doctest-f-and-o-and-p-and-g.md)

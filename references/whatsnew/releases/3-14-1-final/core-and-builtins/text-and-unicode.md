# Python 3.14.1 final / core and builtins / text and unicode

[gh-139516](https://github.com/python/cpython/issues/139516): Resolve the tokenizer issue where a lambda colon wrongly begins a format spec inside an f-string.

[gh-58124](https://github.com/python/cpython/issues/58124): Correct the Python encoding name within Unicode errors of the code page codec: adopt “cp65000” plus “cp65001” in place of “CP_UTF7” and “CP_UTF8”, since those are not valid Python code names. Victor Stinner supplied the patch.

[gh-138558](https://github.com/python/cpython/issues/138558): Correct how unusual t-string annotations are handled within annotationlib. Dave Peck supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

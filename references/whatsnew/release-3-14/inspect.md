# What's new in Python 3.14 / inspect - annotationlib, inspect

### inspect

- A fresh argument *annotation_format* now lets [`signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) pick which [`annotationlib.Format`](https://docs.python.org/3.14/library/annotationlib.html#annotationlib.Format) represents annotations. (Contributed by Jelle Zijlstra in [gh-101552](https://github.com/python/cpython/issues/101552).)

- A fresh argument *unquote_annotations* now reaches [`Signature.format()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.format). When set true, string [annotations](https://docs.python.org/3.14/glossary.html#term-annotation) appear with no surrounding quotes. (Contributed by Jelle Zijlstra in [gh-101552](https://github.com/python/cpython/issues/101552).)

- The new function [`ispackage()`](https://docs.python.org/3.14/library/inspect.html#inspect.ispackage) reports whether some object is a [package](https://docs.python.org/3.14/glossary.html#term-package). (Contributed by Zhikang Yan in [gh-125634](https://github.com/python/cpython/issues/125634).)

[Subject index](INDEX.md) · [Previous source section](imaplib.md) · [Next source section](io.md) · [Release/subject declaration](summary-release-highlights.md)

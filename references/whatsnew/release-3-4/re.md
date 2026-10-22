# What's New In Python 3.4 / re — re

### re

A fresh [`fullmatch()`](https://docs.python.org/3.14/library/re.html#re.fullmatch) function plus the [`Pattern.fullmatch()`](https://docs.python.org/3.14/library/re.html#re.Pattern.fullmatch) method pin the pattern against both ends of the target string. This offers a clear way to state the intent of the match, sidestepping a family of subtle bugs in which `$` characters vanish amid code edits or when alternatives are tacked onto an existing regular expression. (Contributed by Matthew Barnett in [bpo-16203](https://bugs.python.org/issue?@action=redirect&bpo=16203).)

For [regex objects](https://docs.python.org/3.14/library/re.html#re-objects), the repr now carries both the pattern text and the flags; for [match objects](https://docs.python.org/3.14/library/re.html#match-objects), the repr now carries the start index, the end index, plus the substring portion that was matched. (Contributed by Hugo Lopes Tavares and Serhiy Storchaka in [bpo-13592](https://bugs.python.org/issue?@action=redirect&bpo=13592) and [bpo-17087](https://bugs.python.org/issue?@action=redirect&bpo=17087).)

[Subject index](INDEX.md) · [Previous source section](pydoc.md) · [Release/subject declaration](release-highlights.md) · [Next source section](resource.md)

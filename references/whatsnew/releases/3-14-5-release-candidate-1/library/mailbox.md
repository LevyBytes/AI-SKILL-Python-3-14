# Python 3.14.5 release candidate 1 / library / mailbox

[gh-148518](https://github.com/python/cpython/issues/148518): When an email whose address header trailed off in an unclosed double quote was read under any non-`compat32` policy, reaching for the `username` attribute on the mailbox obtained through that header object produced an `IndexError`. The attribute now properly yields an empty string instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

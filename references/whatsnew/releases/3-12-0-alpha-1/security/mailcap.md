# Python 3.12.0 alpha 1 / security / mailcap

[gh-68966](https://github.com/python/cpython/issues/68966): The deprecated mailcap module will no longer slip unsafe text (filenames, MIME types, parameters) into shell commands. Rather than feeding such text through, it emits a warning and behaves as though no match turned up (or, for test commands, as though the test came back false).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

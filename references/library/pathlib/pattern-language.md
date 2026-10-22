# pathlib — Pattern language

### Pattern language

Within patterns handed to `full_match()`, `glob()` and `rglob()`, these wildcards are recognized:

`**` (entire segment)

Matches any number of file or directory segments, including zero.

`*` (entire segment)

Matches one file or directory segment.

`*` (part of a segment)

Matches any number of non-separator characters, including zero.

`?`

Matches one non-separator character.

`[seq]`

Matches a single character drawn from *seq*, with *seq* being a run of characters. Range expressions work too; `[a-z]`, for instance, matches any lowercase ASCII letter. You can stack ranges as well: `[a-zA-Z0-9_]` matches any ASCII letter, digit, or underscore.

`[!seq]`

Matches a single character absent from *seq*, with *seq* obeying the very same rules described above.

To match literally, enclose the meta-characters within brackets. As an example, `"[?]"` matches the character `"?"`.

It's the “`**`” wildcard that switches on recursive globbing. Here are a couple of examples:

| Pattern | Meaning |
| --- | --- |
| “`**/*`” | Every path holding one or more segments. |
| “`**/*.py`” | Every path whose closing segment ends in “`.py`”. |
| “`assets/**`” | Every path that opens with “`assets/`”. |
| “`assets/**/*`” | Every path that opens with “`assets/`”, leaving out “`assets/`” on its own. |

Note

A glob using the “`**`” wildcard walks through each directory across the tree. Hunting through large directory trees can drag on.

Changed in version 3.13: A glob whose pattern closes with “`**`” now yields files as well as directories. Earlier releases yielded directories alone.

Within `Path.glob()` and `rglob()`, appending a trailing slash to the pattern restricts the match to directories only.

Changed in version 3.11: A glob whose pattern closes with a pathname-components separator ([`sep`](https://docs.python.org/3.14/library/os.html#os.sep) or [`altsep`](https://docs.python.org/3.14/library/os.html#os.altsep)) yields directories only.

[Subject index](INDEX.md) · [Previous](path-owner-to-path-lchmod.md) · [Continue](comparison-to-the-glob-module.md) · [Owning module, declaration or section: pathlib](pathlib-object-oriented-filesystem-paths.md)

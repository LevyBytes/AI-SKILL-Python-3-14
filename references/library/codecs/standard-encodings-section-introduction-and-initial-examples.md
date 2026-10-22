# codecs — Standard Encodings — Section introduction and initial examples

### Standard Encodings

Python ships with a range of built-in codecs, realized either as C functions or via dictionaries serving as mapping tables. The table that follows enumerates the codecs by name, alongside a handful of common aliases plus the languages the encoding is apt to serve. Neither the alias roster nor the language roster is intended to be complete. Bear in mind that spelling variants differing only in case or substituting a hyphen for an underscore also count as valid aliases, since they come out equivalent once `normalize_encoding()` normalizes them. To illustrate, `'utf-8'` stands as a valid alias for the `'utf_8'` codec.

Note

The table below enumerates the most common aliases; for an exhaustive list, consult the source [aliases.py](https://github.com/python/cpython/tree/3.14/Lib/encodings/aliases.py) file.

On Windows, `cpXXX` codecs exist for every code page. Yet only the codecs the following table names are guarantead to be present on other platforms.

**CPython implementation detail:** A handful of common encodings can skip past the codecs lookup machinery for a performance gain. CPython acknowledges these optimization opportunities solely for a narrow set of (case insensitive) aliases: utf-8, utf8, latin-1, latin1, iso-8859-1, iso8859-1, mbcs (Windows only), ascii, us-ascii, utf-16, utf16, utf-32, utf32, plus the same spellings with underscores swapped in for dashes. Reaching for other aliases of these encodings can lead to slower running.

Changed in version 3.6: Optimization opportunity recognized for us-ascii.

A good many of the character sets cover the same languages. Where they differ is in particular characters (for example, whether the EURO SIGN is included) and in how characters get assigned to code positions. Among the European languages especially, the variants below tend to show up:

- an ISO 8859 codeset

- a Microsoft Windows code page, generally built off an 8859 codeset yet swapping out control characters for extra graphic characters

- an IBM EBCDIC code page

- an IBM PC code page, which is ASCII compatible

[Subject index](INDEX.md) · [Previous](encodings-and-unicode.md) · [Continue](standard-encodings-east-asian-and-ascii-encodings.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)

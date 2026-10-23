# What's New In Python 3.3 / codecs - codecs

### codecs

A rewrite of the [`mbcs`](https://docs.python.org/3.14/library/codecs.html#module-encodings.mbcs) codec makes it deal correctly with the `replace` and `ignore` error handlers across every Windows version. Where the `mbcs` codec once offered only `replace` for encoding and `ignore` for decoding, it now backs all error handlers.

One Windows-only codec was added: `cp65001` ([bpo-13216](https://bugs.python.org/issue?@action=redirect&bpo=13216)). This is Windows code page 65001 (Windows UTF-8, `CP_UTF8`). For instance, `sys.stdout` uses it whenever the console output code page is switched to cp65001 (say, by running the `chcp 65001` command).

Resynchronization is now quicker in multibyte CJK decoders. Out of an invalid byte sequence they discard only its leading byte. To illustrate, `b'\xff\n'.decode('gb2312', 'replace')` now yields a `\n` trailing the substituted replacement glyph.

([bpo-12016](https://bugs.python.org/issue?@action=redirect&bpo=12016))

Calls to the encode() methods of an incremental CJK codec encoder will no longer clear it each time. To demonstrate:

```python
>>> import codecs
>>> encoder = codecs.getincrementalencoder('hz')('strict')
>>> b''.join(encoder.encode(x) for x in '\u52ff\u65bd\u65bc\u4eba\u3002 Bye.')
b'~{NpJ)l6HK!#~} Bye.'

```

Run under earlier Python releases, the same snippet instead yields `b'~{Np~}~{J)~}~{l6~}~{HK~}~{!#~} Bye.'`.

([bpo-12100](https://bugs.python.org/issue?@action=redirect&bpo=12100))

The `unicode_internal` codec has been deprecated.

[Subject index](INDEX.md) · [Previous source section](bz2.md) · [Next source section](collections.md) · [Release/subject declaration](summary-release-highlights.md)

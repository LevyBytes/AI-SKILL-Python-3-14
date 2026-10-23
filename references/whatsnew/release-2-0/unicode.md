# What’s New in Python 2.0 / Unicode - codecs, re, unicodedata

### Unicode

The biggest fresh capability in Python 2.0 is a brand-new core data type: Unicode strings. Unicode relies on 16-bit numbers for representing characters rather than the 8-bit number that ASCII employs, which means 65,536 separate characters can be handled.

The eventual interface for Unicode support emerged from innumerable, frequently heated debates on the python-dev mailing list, and was largely built by Marc-André Lemburg, drawing on a Unicode string type implementation from Fredrik Lundh. A thorough description of the interface was recorded as [**PEP 100**](https://peps.python.org/pep-0100/), “Python Unicode Integration”. Here we’ll just touch on the most important aspects of the Unicode interfaces.

Within Python source code, Unicode strings appear as `u"string"`. Any Unicode character at all can be expressed via a new escape sequence, `\u*HHHH*`, in which *HHHH* is a 4-digit hexadecimal number ranging from 0000 to FFFF. You may also reuse the existing `\x*HH*` escape sequence, and octal escapes work for characters as high as U+01FF, which `\777` represents.

Like ordinary strings, Unicode strings form an immutable sequence type. They support indexing and slicing, yet can’t be altered in place. Unicode strings provide an `encode( [encoding] )` method that yields an 8-bit string in whichever encoding you want. Encodings get named with strings, for instance `'ascii'`, `'utf-8'`, `'iso-8859-1'`, and so on. A codec API exists for building and registering new encodings, which then become usable across an entire Python program. When no encoding is given, the default is normally 7-bit ASCII, though you can alter it for your Python installation by invoking the `sys.setdefaultencoding(encoding)` function inside a customized version of `site.py`.

Mixing 8-bit and Unicode strings always promotes to Unicode, applying the default ASCII encoding; thus `'a' + u'bc'` produces `u'abc'`.

Fresh built-in functions were introduced, and certain existing built-ins were adjusted to handle Unicode:

- `unichr(ch)` hands back a Unicode string 1 character in length, holding the character *ch*.

- `ord(u)`, in which *u* is a 1-character regular or Unicode string, gives back that character’s number as an integer.

- `unicode(string [, encoding] [, errors] )` builds a Unicode string out of an 8-bit string. `encoding` is a string that names which encoding to apply. The `errors` parameter dictates how characters invalid for the current encoding are handled; supplying `'strict'` as the value triggers an exception whenever an encoding error occurs, while `'ignore'` lets errors pass silently and `'replace'` substitutes U+FFFD, the official replacement character, when anything goes wrong.

- The `exec` statement, plus assorted built-ins like `eval()`, `getattr()`, and `setattr()`, will likewise take Unicode strings in addition to regular strings. (It’s conceivable that the work of fixing this overlooked a few built-ins; should you spot a built-in function that takes strings yet rejects Unicode strings altogether, please file it as a bug.)

A fresh module, [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata), exposes an interface to Unicode character properties. As an example, `unicodedata.category(u'A')` yields the 2-character string ‘Lu’, where the ‘L’ marks it as a letter and the ‘u’ signals that it’s uppercase. `unicodedata.bidirectional(u'\u0660')` returns ‘AN’, indicating that U+0660 is an Arabic number.

The [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module holds functions for looking up existing encodings and registering new ones. Unless you’re writing a new encoding yourself, you’ll most commonly reach for the `codecs.lookup(encoding)` function, which gives back a 4-element tuple: `(encode_func, decode_func, stream_reader, stream_writer)`.

- *encode_func* names a function whose input is a Unicode string and whose output is a 2-tuple `(string, length)`. Here *string* holds, as an 8-bit string, some portion (perhaps the entirety) of the Unicode string rendered into the chosen encoding, while *length* reports how much of the Unicode string got converted.

- *decode_func* is the reverse of *encode_func*, accepting an 8-bit string and returning a 2-tuple `(ustring, length)`, made up of the resulting Unicode string *ustring* and the integer *length* stating how much of the 8-bit string was consumed.

- *stream_reader* is a class enabling decoding of input drawn from a stream. *stream_reader(file_obj)* gives back an object offering the `read()`, `readline()`, and `readlines()` methods. Each of these methods translates from the chosen encoding and returns Unicode strings.

- *stream_writer*, in the same vein, is a class enabling encoding of output to a stream. *stream_writer(file_obj)* gives back an object offering the `write()` and `writelines()` methods. These methods anticipate Unicode strings, converting them to the chosen encoding as they’re written.

By way of example, the code below writes a Unicode string out to a file, encoding it as UTF-8:

```python
import codecs

unistr = u'\u0660\u2000ab ...'

(UTF8_encode, UTF8_decode,
 UTF8_streamreader, UTF8_streamwriter) = codecs.lookup('UTF-8')

output = UTF8_streamwriter( open( '/tmp/output', 'wb') )
output.write( unistr )
output.close()

```

This next snippet would then read the UTF-8 input back out of the file:

```python
input = UTF8_streamreader( open( '/tmp/output', 'rb') )
print repr(input.read())
input.close()

```

Unicode-aware regular expressions come courtesy of the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, whose new underlying engine, dubbed SRE, was written by Fredrik Lundh of Secret Labs AB.

A `-U` command line option was introduced that tells the Python compiler to treat every string literal as a Unicode string literal. The intent is to support testing and future-proofing your Python code, given that some later version of Python might discontinue 8-bit strings and supply Unicode strings exclusively.

[Subject index](INDEX.md) · [Previous source section](new-development-process.md) · [Next source section](list-comprehensions.md) · [Release/subject declaration](introduction.md)

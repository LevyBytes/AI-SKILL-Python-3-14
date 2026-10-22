# codecs — Encodings and Unicode

### Encodings and Unicode

Internally, strings live as sequences of code points spanning `U+0000`–`U+10FFFF`. (Consult [**PEP 393**](https://peps.python.org/pep-0393/) for fuller detail on the implementation.) The moment a string object travels beyond CPU and memory, endianness — and the manner in which these arrays land as bytes — turns into a concern. Just as with other codecs, turning a string into a byte sequence is termed *encoding*, while rebuilding the string back out of the byte sequence is termed *decoding*. A whole assortment of text serialisation codecs exists, gathered together under the name [text encodings](https://docs.python.org/3.14/glossary.html#term-text-encoding).

The most basic text encoding (going by `'latin-1'` or `'iso-8859-1'`) pairs the code points 0–255 with the bytes `0x0`–`0xff`, so a string object holding any code point past `U+00FF` cannot be encoded through this codec. Attempting it triggers a [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) resembling what follows (though the precise wording of the message can vary): `UnicodeEncodeError: 'latin-1' codec can't encode character '\u1234' in position 3: ordinal not in range(256)`.

A separate family of encodings (dubbed the charmap encodings) picks out some other subset of every Unicode code point along with how those code points line up against the bytes `0x0`–`0xff`. For a look at how that works, just crack open something like `encodings/cp1252.py` (an encoding employed chiefly on Windows). Inside sits a string constant of 256 characters revealing which character corresponds to each byte value.

Every one of these encodings can represent merely 256 out of the 1114112 code points Unicode defines. One plain, no-frills scheme capable of holding any Unicode code point stores each code point across four back-to-back bytes. Two arrangements present themselves: lay the bytes down in big endian or in little endian order. The names for these two encodings are `UTF-32-BE` and `UTF-32-LE` accordingly. The drawback is that should you, say, run `UTF-32-BE` on a little endian machine, you'll forever be swapping bytes while encoding and decoding. Python's `UTF-16` and `UTF-32` codecs sidestep this snag by adopting the platform's native byte order whenever no BOM is present. Python goes with prevailing platform practice, so native-endian data round-trips without superfluous byte swapping, even though the Unicode Standard falls back to big-endian when no byte order is stated. Once those bytes get read by a CPU of opposite endianness, the bytes must be swapped. So that the endianness of a `UTF-16` or `UTF-32` byte sequence can be spotted, a BOM (“Byte Order Mark”) comes into play. It is the Unicode character `U+FEFF`. You can stick this character ahead of any `UTF-16` or `UTF-32` byte sequence. The byte-swapped form of this character (`0xFFFE`) is an illegal character forbidden from appearing within Unicode text. Whenever the opening character of a `UTF-16` or `UTF-32` byte sequence reads `U+FFFE`, the bytes have to be swapped during decoding.

Regrettably the character `U+FEFF` carried a second duty as a `ZERO WIDTH NO-BREAK SPACE`: a character lacking any width that bars a word from being broken apart. One could, for instance, employ it to feed cues to a ligature algorithm. As of Unicode 4.0, treating `U+FEFF` as a `ZERO WIDTH NO-BREAK SPACE` has been deprecated (with `U+2060` (`WORD JOINER`) taking over that duty). Even so, Unicode software has to remain capable of coping with `U+FEFF` in either capacity: when it's a BOM it acts as a means of pinning down the storage layout of the encoded bytes, then disappears the instant the byte sequence becomes a decoded string; when it's a `ZERO WIDTH NO-BREAK SPACE` it's an ordinary character decoded like any other.

One further encoding can cover the whole span of Unicode characters: UTF-8. UTF-8 is an 8-bit encoding, so byte order poses no problems within UTF-8. Every byte in a UTF-8 byte sequence breaks into two pieces: marker bits (the most significant ones) and payload bits. The marker bits form a run of anywhere from zero to four `1` bits capped by a `0` bit. Unicode characters get encoded as follows (with x standing for payload bits that, once strung together, yield the Unicode character):

| Range | Encoding |
| --- | --- |
| `U-00000000` … `U-0000007F` | 0xxxxxxx |
| `U-00000080` … `U-000007FF` | 110xxxxx 10xxxxxx |
| `U-00000800` … `U-0000FFFF` | 1110xxxx 10xxxxxx 10xxxxxx |
| `U-00010000` … `U-0010FFFF` | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

The Unicode character's least significant bit is the x bit furthest to the right.

Because UTF-8 is an 8-bit encoding, no BOM is needed, and any `U+FEFF` character within the decoded string (the opening character included) counts as a `ZERO WIDTH NO-BREAK SPACE`.

Lacking outside information, there's no dependable way to figure out which encoding produced a given string. Any charmap encoding is able to decode whatever random byte sequence it's handed. That, however, doesn't hold for UTF-8, since UTF-8 byte sequences follow a structure that rules out arbitrary byte sequences. To bolster how dependably a UTF-8 encoding can be spotted, Microsoft cooked up a UTF-8 variant (which Python names `"utf-8-sig"`) for its Notepad application: ahead of writing any Unicode characters to the file, a UTF-8 encoded BOM (appearing as this byte sequence: `0xef`, `0xbb`, `0xbf`) gets written. Because it's fairly unlikely that any charmap encoded file would open with these byte values (which might, for example, map to

>   LATIN SMALL LETTER I WITH DIAERESIS RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK INVERTED QUESTION MARK

in iso-8859-1), this raises the odds that a `utf-8-sig` encoding can be guessed accurately out of the byte sequence. Thus in this case the BOM isn't there to pin down the byte order used in producing the byte sequence, but rather as a signature aiding the encoding guess. While encoding, the utf-8-sig codec writes `0xef`, `0xbb`, `0xbf` as the file's opening three bytes. While decoding, `utf-8-sig` drops those three bytes when they show up as the file's opening three bytes. Within UTF-8, relying on the BOM is discouraged and is best steered clear of in general.

[Subject index](INDEX.md) · [Previous](codecs-streamrecoder-class.md) · [Continue](standard-encodings-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)

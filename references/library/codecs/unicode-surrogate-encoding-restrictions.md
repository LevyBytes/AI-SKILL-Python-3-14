# codecs - Standard Encodings - Contract: Changed in version 3.4: Encoding of surrogate code points (`U+D800`–`U+DFFF`) is no longer permitted by the utf-16* and utf-32* encoders.

Changed in version 3.4: Encoding of surrogate code points (`U+D800`–`U+DFFF`) is no longer permitted by the utf-16* and utf-32* encoders. Byte sequences that map onto surrogate code points are, likewise, no longer decoded by the utf-32* decoders.

Changed in version 3.8: `cp65001` is now an alias to `utf_8`.

Changed in version 3.14: On Windows, every code page now has a `cpXXX` codec on hand.

[Subject index](INDEX.md) · [Previous](standard-encodings-unicode-encodings.md) · [Continue](python-specific-encodings.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Owning module, declaration or section: Standard Encodings](standard-encodings-section-introduction-and-initial-examples.md)

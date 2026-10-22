# encodings — `encodings` — Encodings package

### `encodings` — Encodings package

The functions below are what this module provides:

 encodings.normalize_encoding(*encoding*)

Put the encoding name *encoding* into normalized form.

Here is how the normalization proceeds: every non-alphanumeric character, save the dot reserved for Python package names, is gathered up and swapped for one underscore, after which any underscores at the start or end are stripped. As an example, `' -;#'` turns into `'_'`.

Keep in mind that *encoding* ought to contain ASCII alone.

Note

Outside of testing, steer clear of calling the functions below yourself; lean on `codecs.lookup()` in their stead.

 encodings.search_function(*encoding*)

Hunt for whichever codec module matches the supplied encoding name *encoding*.

To begin, the function runs *encoding* through `normalize_encoding()`, then hunts for a matching alias. It tries importing a codec module out of the encodings package by way of either that alias or the normalized name. Provided the module turns up and declares a working `getregentry()` function yielding a `codecs.CodecInfo` object, the codec gets cached and returned.

Should the codec module declare a `getaliases()` function, whatever aliases it yields are registered so they can be used later.

 encodings.win32_code_page_search_function(*encoding*)

Hunt for a Windows code page encoding *encoding* shaped like `cpXXXX`.

Where the code page proves valid and supported, give back a matching `codecs.CodecInfo` object.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.14.

The exception below is what this module provides:

 *exception *encodings.CodecRegistryError

Thrown whenever a codec turns out to be invalid or incompatible.

[Subject index](INDEX.md) · [Previous](../codecs/text-transforms.md) · [Continue](../encodings-idna/encodings-idna-nameprep-to-encodings-idna-tounicode.md)

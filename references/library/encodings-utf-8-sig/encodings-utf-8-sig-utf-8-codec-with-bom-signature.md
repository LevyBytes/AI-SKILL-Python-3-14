# encodings.utf_8_sig — `encodings.utf_8_sig` — UTF-8 codec with BOM signature

### `encodings.utf_8_sig` — UTF-8 codec with BOM signature

What this module provides is a variant of the UTF-8 codec. While encoding, a UTF-8 encoded BOM gets placed ahead of the UTF-8 encoded bytes. The stateful encoder does so a single time only, on its first write to the byte stream. While decoding, any optional UTF-8 encoded BOM sitting at the front of the data is passed over.

[Subject index](INDEX.md) · [Previous](../encodings-mbcs/encodings-mbcs-windows-ansi-codepage.md)
